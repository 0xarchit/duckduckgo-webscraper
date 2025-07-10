# Cloudflare Worker: Jina AI & Groq Scraper

This Cloudflare Worker fetches search results via [Jina AI](https://jina.ai), retrieves page content, analyzes it with Groq LLM API, and rotates through multiple API keys using GetPantry.

## Setup

1. Update API Keys and Pantry Config
   - Open `worker.js` in this folder.
   - In `JINA_API_KEYS` and `GROQ_API_KEYS`, replace placeholder strings with your API keys (comma-separated).
   - Set `PANTRY_ID` and `BASKET_NAME` to match your GetPantry identifiers.

2. Initialize Pantry Basket
   - In your GetPantry basket, seed the following JSON:
     ```json
     {
       "jina": 0,
       "groq": 0
     }
     ```

3. Deploy to Cloudflare Workers
   - Create a cloudflare worker from dashboard
   - Replace the exsisting code with this code 

4. Invoke the Worker
   - Send a GET request:
     ```
     GET https://<your-worker>/?query=your+search+term
     ```
   - The response JSON includes `urls` and detailed `contents` analyses.
  
## Demo

Curious how it works before deploying?  
Try it live with a test query with test api key (max 10 per day):

```bash
GET https://pagescrape.0xcloud.workers.dev/?query=web+scraping&key=test
```

🔍 The response will include a object containing a list of relevant URLs and in-depth content analysis powered by Groq LLM.

## License

MIT
