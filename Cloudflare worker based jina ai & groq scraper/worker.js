addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

const JINA_API_KEYS = [
  'list of comma seprated jina api keys here you can add multiple or single api key'
];

const GROQ_API_KEYS = [
  'list of comma seprated groq api keys here you can add multiple or single api key'
];

const PANTRY_ID = 'pantry id here get from https://getpantry.cloud';
const BASKET_NAME = 'name of your pantry basket create from pantry dashboard';
/*
put this json in pantry bucket:

{
  "jina": 0,
  "groq": 0
}

*/


async function getApiIndices() {
  const url = `https://getpantry.cloud/apiv1/pantry/${PANTRY_ID}/basket/${BASKET_NAME}`;
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    });
    if (!response.ok) throw new Error('Failed to fetch indices');
    const data = await response.json();
    return { jina: data.jina || 0, groq: data.groq || 0 };
  } catch (e) {
    console.error('Error fetching indices:', e.message);
    return { jina: 0, groq: 0 };
  }
}

async function updateApiIndices(jinaIndex, groqIndex) {
  const url = `https://getpantry.cloud/apiv1/pantry/${PANTRY_ID}/basket/${BASKET_NAME}`;
  try {
    await fetch(url, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ jina: jinaIndex, groq: groqIndex })
    });
  } catch (e) {
    console.error('Error updating indices:', e.message);
  }
}

function getNextApiKey(keys, currentIndex) {
  const nextIndex = (currentIndex + 1) % keys.length;
  return { key: keys[currentIndex], nextIndex };
}

async function handleRequest(request) {
  if (request.method !== 'GET') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), {
      status: 405,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  try {
    const url = new URL(request.url);
    const query = url.searchParams.get('query');
    if (!query) {
      return new Response(JSON.stringify({ error: 'Query is required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const indices = await getApiIndices();
    const jinaApi = getNextApiKey(JINA_API_KEYS, indices.jina);
    const groqApi = getNextApiKey(GROQ_API_KEYS, indices.groq);

    const urls = await getJinaSearchLinks(query, jinaApi.key);
    const contents = [];
    let processed = 0;
    for (const url of urls) {
      if (processed >= 5) break;
      if (url.includes('linkedin.com')) continue;
      try {
        const content = await fetchUrlContentViaJina(url, jinaApi.key);
        const groqResponse = await getGroqResponse(content, groqApi.key);
        contents.push({ 
          url, 
          status: 'success', 
          analyse: groqResponse 
        });
        processed++;
      } catch (e) {
        contents.push({ 
          url, 
          status: 'error', 
          error: e.message, 
          analysee: '' 
        });
        processed++;
      }
    }

    await updateApiIndices(jinaApi.nextIndex, groqApi.nextIndex);

    const response = { urls: urls.slice(0, 5), contents };
    return new Response(JSON.stringify(response), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (e) {
    return new Response(JSON.stringify({ error: `Unexpected error: ${e.message}` }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}

async function getJinaSearchLinks(query, jinaApiKey) {
  const encodedQuery = query.replace(/\s+/g, '+');
  const searchUrl = `https://s.jina.ai/${encodedQuery}`;
  const headers = { 
    'User-Agent': 'Mozilla/5.0',
    'Authorization': `Bearer ${jinaApiKey}`,
    'Accept': 'application/json',
    'X-Respond-With': 'json'
  };
  try {
    const response = await fetch(searchUrl, { headers });
    if (!response.ok) {
      console.error('Jina API status:', response.status, await response.text());
      throw new Error(`Search request failed: ${response.status}`);
    }

    const text = await response.text();
    let data;
    try {
      data = JSON.parse(text);
    } catch (e) {
      console.error('Invalid Jina API response:', text);
      return [];
    }

    if (!data.data || !Array.isArray(data.data)) {
      console.error('Unexpected Jina API response structure:', data);
      return [];
    }

    return data.data.map(item => item.url).filter(url => url).slice(0, 6);
  } catch (e) {
    console.error('Jina search error:', e.message);
    return [];
  }
}

async function fetchUrlContentViaJina(url, jinaApiKey) {
  const proxyUrl = `https://r.jina.ai/${url}`;
  const headers = { 
    'User-Agent': 'Mozilla/5.0',
    'Authorization': `Bearer ${jinaApiKey}`
  };
  const response = await fetch(proxyUrl, { headers });

  if (!response.ok) {
    throw new Error(`Content request failed: ${response.status}`);
  }

  const text = await response.text();
  return text.slice(0, 25000);
}

async function getGroqResponse(content, groqApiKey) {
  const groqUrl = 'https://api.groq.com/openai/v1/chat/completions';
  const headers = {
    'Authorization': `Bearer ${groqApiKey}`,
    'Content-Type': 'application/json'
  };
  const payload = {
    model: 'meta-llama/llama-4-scout-17b-16e-instruct',
    messages: [
      {
        role: 'user',
        content: `Perform a detailed research analysis on the following content, identifying key themes, insights, and implications return only analyses, links present in content, images links, contact like email or phone separatly: ${content}`
      }
    ],
    max_tokens: 5000,
    temperature: 0.7
  };

  const response = await fetch(groqUrl, {
    method: 'POST',
    headers,
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    throw new Error(`Groq API request failed: ${response.status}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}