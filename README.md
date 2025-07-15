# DuckDuckGo Query Scraper

A simple Python-based web scraper that uses DuckDuckGo Lite search to fetch top result pages, then extracts structured content (titles, descriptions, headings, summaries, links, and more) from each page.

🌟 Give this repo a star to show support 🌟

## Features

- Uses DuckDuckGo Lite search for query results
- Automatically rotates through a free proxy list sourced from GitHub
- Parses and extracts:
  - Page title, meta description, and main heading
  - First few paragraphs as a summary
  - External, internal, and social links
  - Email/contact info and keywords
  - Author and publication date (if available)
  - JSON-LD structured data when present
- Handles DuckDuckGo redirect links and skips ad redirects
- Gracefully falls back when pages fail to load via proxy

## Web Interface (FastAPI + Tailwind CSS)

A modern web UI to demo and visualize scraping results in your browser.

- Install additional dependencies:
  ```powershell
  pip install fastapi uvicorn[standard] jinja2
  ```
- Run the FastAPI server:
  ```powershell
  uvicorn app:app --reload --host 0.0.0.0 --port 8000
  ```
- Open your browser at http://localhost:8000
- Enter a search query, select or provide a proxy list, and watch the live loading animation while results are fetched and displayed.

The web interface features:
- Dropdown menu to choose from preset proxy lists or enter a custom URL
- Loading overlay with spinner and warning message
- Styled result cards showing metadata and content excerpts

For a minimal, standalone scraper script without FastAPI, see `basescript/scraper_base.py` in the `basescript/` folder.

## Installation of Script

1. Clone this repository:
   ```powershell
   git clone https://github.com/0xarchit/duckduckgo-webscraper.git
   cd duckduckgo-webscraper
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

## Proxy List

This project maintains a free, public proxy list for scraping, automatically updated every 20 minutes via GitHub Actions. The list is sourced from multiple providers and tested for working status before publishing.

- **Latest proxy list (auto-updated 20mins):**  
  https://raw.githubusercontent.com/0xarchit/duckduckgo-webscraper/refs/heads/main/proxies.txt

The update workflow fetches fresh proxies, tests them, and commits the results to the repository every 20 minutes.  
You can use this list directly in your own scraping projects or scripts.

> **Note:** Free proxies may be slow or unreliable. For best results, consider using a

Run the scraper and enter your search query (single or multi-word):
```powershell
python basescript\scraper_base.py
```

The tool uses free proxy lists fetched from GitHub, so it can be relatively slow. If you need faster and more reliable scraping, consider using a paid proxy list and update the `fetch_proxies()` URL accordingly.

## Configuration

- Proxy list URL is defined in `fetch_proxies()` within `webscrapper.py`.
- Adjust `max_results` to change the number of pages scraped per query.
- Modify delays (`time.sleep()`) to tune rate limits.

## Sample Output

<details>
  <summary>Click to expand output content</summary>

```text

======================================================================
                     🌐 DuckDuckGo Query Scraper 🌐
                            By 0xArchit
======================================================================

🔎 Enter your search query: Gen AI
🚀 Fetching fresh proxy list...
✅ Loaded 2393 proxies.

🔍 Initiating DuckDuckGo Lite search for: 'Gen AI'

🔌 Testing proxy: 51.81.245.3:17981
✅ Proxy working: 51.81.245.3:17981
🌐 Attempt 1/5 Scraping: https://lite.duckduckgo.com/lite/?q=Gen AI with proxy: http://51.81.245.3:17981
  ✅ Successfully scraped https://lite.duckduckgo.com/lite/?q=Gen AI
⏳ Waiting 5 seconds after DuckDuckGo search to avoid rate limits...

➡️ Found result: 'What is generative AI? - IBM'
   🔗 Link: https://www.ibm.com/think/topics/generative-ai
⏳ Waiting 5 seconds before scraping this result page...
🌐 Attempt 1/5 Scraping: https://www.ibm.com/think/topics/generative-ai with proxy: http://51.81.245.3:17981
  ✅ Successfully scraped https://www.ibm.com/think/topics/generative-ai

➡️ Found result: 'Generative artificial intelligence - Wikipedia'
   🔗 Link: https://en.wikipedia.org/wiki/Generative_artificial_intelligence
⏳ Waiting 5 seconds before scraping this result page...
🌐 Attempt 1/5 Scraping: https://en.wikipedia.org/wiki/Generative_artificial_intelligence with proxy: http://51.81.245.3:17981
  ✅ Successfully scraped https://en.wikipedia.org/wiki/Generative_artificial_intelligence

➡️ Found result: 'What is Generative AI? - GeeksforGeeks'
   🔗 Link: https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/
⏳ Waiting 5 seconds before scraping this result page...
🌐 Attempt 1/5 Scraping: https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/ with proxy: http://51.81.245.3:17981
  ✅ Successfully scraped https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/

==================== UNIVERSAL SCRAPE REPORT ====================


---------- ✨ RESULT #1 ✨ ----------------------------------------

  📌 Title: What is generative AI? - IBM
  🌐 URL  : https://www.ibm.com/think/topics/generative-ai

  📊 Detailed Analysis (General Web Page):
    - Url: https://www.ibm.com/think/topics/generative-ai
    - Title: What is Generative AI?  | IBM
    - Meta Description: Generative AI is artificial intelligence (AI) that can create original content in response to a user’s prompt or request.
    - Main Heading: What is generative AI?
    - Summary Text: Editorial Lead, AI Models  Editor, Topics & Insights for IBM Think  Generative AI, sometimes calledgen AI,isartificial intelligence(AI) that can create original content such as text, images, video, audio or software code in response to a user’s prompt or request.
    - Links: (Complex Data - See raw content)
    - Email: xxx@ccc.com
    - Keywords: Generative AI
    - Author: Cole Stryker
    - Published Date: Not specified
    - Structured Data: (Complex Data - See raw content)

  📄 Raw Content Excerpt:
    What is Generative AI? | IBM What is generative AI? 22 March 2024
    Link copied Authors Cole Stryker Editorial Lead, AI Models Mark
    Scapicchio Editor, Topics & Insights for IBM Think What is
    generative AI? Generative AI, sometimes called gen AI, is
    artificial intelligence (AI) that can create original content such
    as text, images, video, audio or software code in response to a
    user’s prompt or request. Generative AI relies on sophisticated
    machine learning models called deep learning models algorithms
    that simulate the learning and decision-making processes of the
    human brain. These models work by identifying and encoding the
    patterns and relationships in huge amounts of data, and then using
    that information to understand users' natural language requests or
    questions and respond with relevant new content. AI has been a hot
    technology topic for the past decade, but generative AI, and
    specifically the arrival of ChatGPT in 2022, has thrust AI into
    worldwide headlines and launched an unprecedented surge of AI
    innovation and adoption. Generative AI offers enormous
    productivity benefits for individuals and organizations, and while
    it also presents very real challenges and risks, businesses are
    forging ahead, exploring how the technology can improve their
    internal workflows and enrich their products and services.
    According to research by the management consulting firm McKinsey,
    one third of organizations are already using generative AI
    regularly in at least one business function.¹ Industry analyst
    Gartner projects more than 80% of organizations will have deployed
    generative AI applications or used generative AI application
    programming interfaces (APIs) by 2026. 2 How generative AI works
    For the most part, generative AI operates in three phases:
    Training , to create a foundation model that can serve as the
    basis of multiple gen AI applications. Tuning , to tailor the
    foundation model to a specific gen AI application. Generation ,
    evaluation and retuning , to assess the gen AI application's
    output and continually improve its quality and accuracy. Training
    Generative AI begins with a foundation model, a deep learning
    model that serves as the basis for multiple different types of
    generative AI applications. The most common foundation models
    today are large language models (LLMs) , created for text
    generation applications, but there are also foundation models for
    image generation, video generation, and sound and music generation
    as well as multimodal foundation models that can support several
    kinds content generation. To create a foundation model,
    practitioners train a deep learning algorithm on huge volumes of
    raw, unstructured, unlabeled data e.g., terabytes of data culled
    from the internet or some other huge data source. During training,
    the algorithm performs and evaluates millions of ‘fill in the
    blank’ exercises, trying to predict the next element in a sequence
    e.g., the next word in a sentence, the next element in an image,
    the next command in a line of code and continually adjusting
    itself to minimize the difference between its predictions and the
    actual data (or ‘correct’ result). The result of this training is
    a neural network of parameters, encoded representations of the
    entities, patterns and relationships in the data, that can
    generate content autonomously in response to inputs, or prompts.
    This training process is compute-intensive, time-consuming and
    expensive: it requires thousands of clustered graphics processing
    units (GPUs) and weeks of processing, all of which costs millions
    of dollars. Open-source foundation model projects, such as Meta's
    Llama-2, enable gen AI developers to avoid this step and its
    costs. Tuning Metaphorically speaking, a foundation model is a
    generalist: It knows a lot about a lot of types of content, but
    often can’t generate specific types of output with desired
    accuracy or fidelity. For that, the model must be tuned to a
    specific content generation task. This can be done in a variety of
    ways. Fine tuning Fine tuning involves feeding the model labeled
    data specific to the content generation application questions or
    prompts the application is likely to receive, and corresponding
    correct answers in the desired format. For example, if a
    development team is trying to create a customer service chatbot,
    it would create hundreds or thousands of documents containing
    labeled customers service questions and correct answers, and then
    feed those documents to the model. Fine-tuning is labor-intensive.
    Developers often outsource the task to companies with large data-
    labeling workforces. Reinforcement learning with human feedback
    (RLHF) In RLHF , human users respond to generated content with
    evaluations the model can use to update the model for greater
    accuracy or relevance. Often, RLHF involves people ‘scoring’
    different outputs in response to the same prompt. But it can be as
    simple as having people type or talk back to a chatbot or virtual
    assistant, correcting its output. Generation, evaluation, more
    tuning Developers and users continually assess the outputs of
    their generative AI apps, and further tune the model even as often
    as once a week for greater accuracy or relevance. (In contrast,
    the foundation model itself is updated much less frequently,
    perhaps every year or 18 months.) Another option for improving a
    gen AI app's performance is retrieval augmented generation (RAG).
    RAG is a framework for extending the foundation model to use
    relevant sources outside of the training data, to supplement and
    refine the parameters or representations in the original model.
    RAG can ensure that a generative AI app always has access to the
    most current information. As a bonus, the additional sources
    accessed via RAG are transparent to users in a way that the
    knowledge in the original foundation model is not. Generative AI
    model architectures and how they have evolved Truly generative AI
    models deep learning models that can autonomously create content
    on demand have evolved over the last dozen years or so. The
    milestone model architectures during that period include
    Variational autoencoders (VAEs) , which drove breakthroughs in
    image recognition, natural language processing and anomaly
    detection. Generative adversarial networks (GANs) and diffusion
    models , which improved the accuracy of previous applications and
    enabled some of the first AI solutions for photo-realistic image
    generation. Transformers , the deep learning model architecture
    behind the foremost foundation models and generative AI solutions
    today. Variational autoencoders (VAEs) An autoencoder is a deep
    learning model comprising two connected neural networks: One that
    encodes (or compresses) a huge amount of unstructured, unlabeled
    training data into parameters, and another that decodes those
    parameters to reconstruct the content. Technically, autoencoders
    can generate new content, but they’re more useful for compressing
    data for storage or transfer, and decompressing it for use, than
    they are for high-quality content generation. Introduced in 2013,
    variational autoencoders (VAEs) can encode data like an
    autoencoder, but decode multiple new variations of the content .
    By training a VAE to generate variations toward a particular goal,
    it can ‘zero in’ on more accurate, higher-fidelity content over
    time. Early VAE applications included anomaly detection (e.g.,
    medical image analysis) and natural language generation.
    Generative adversarial networks (GANs) GANs, introduced in 2014,
    also comprise two neural networks: A generator, which generates
    new content, and a discriminator, which evaluates the accuracy and
    quality the generated data. These adversarial algorithms
    encourages the model to generate increasingly high-quality
    outpits. GANs are commonly used for image and video generation,
    but can generate high-quality, realistic content across various
    domains. They've proven particularly successful at tasks as style
    transfer (altering the style of an image from, say, a photo to a
    pencil sketch) and data augmentation (creating new, synthetic data
    to increase the size and diversity of a training data set).
    Diffusion models Also introduced in 2014, diffusion models work by
    first adding noise to the training data until it’s random and
    unrecognizable, and then training the algorithm to iteratively
    diffuse the noise to reveal a desired output. Diffusion models
    take more time to train than VAEs or GANs, but ultimately offer
    finer-grained control over output, particularly for high-quality
    image generation tool. DALL-E, Open AI’s image-generation tool, is
    driven by a diffusion model. Transformers First documented in a
    2017 paper published by Ashish Vaswani and others, transformers
    evolve the encoder-decoder paradigm to enable a big step forward
    in the way foundation models are trained, and in the quality and
    range of content they can produce. These models are at the core of
    most of today’s headline-making generative AI tools, including
    ChatGPT and GPT-4, Copilot, BERT, Bard, and Midjourney to name a
    few. Transformers use a concept called attention, determining and
    focusing on what’s most important about data within a sequence to;
    process entire sequences of data e.g., sentences instead of
    individual words simultaneously; capture the context of the data
    within the sequence; encode the training data into embeddings
    (also called hyperparameters ) that represent the data and its
    context. In addition to enabling faster training, transformers
    excel at natural language processing (NLP) and natural language
    understanding (NLU), and can generate longer sequences of data
    e.g., not just answers to questions, but poems, articles or papers
    with greater accuracy and higher quality than other deep
    generative AI models. Transformer models can also be trained or
    tuned to use tools e.g., a spreadsheet application, HTML, a
    drawing program to output content in a particular format. What
    generative AI can create Generative AI can create many types of
    content across many different domains. Text Generative models.
    especially those based on transformers, can generate coherent,
    contextually relevant text, everything from instructions and
    documentation to brochures, emails, web site copy, blogs,
    articles, reports, papers, and even creative writing. They can
    also perform repetitive or tedious writing tasks (e.g., such as
    drafting summaries of documents or meta descriptions of web
    pages), freeing writers’ time for more creative, higher-value
    work. Images and video Image generation such as DALL-E, Midjourney
    and Stable Diffusion can create realistic images or original art,
    and can perform style transfer, image-to-image translation and
    other image editing or image enhancement tasks. Emerging gen AI
    video tools can create animations from text prompts, and can apply
    special effects to existing video more quickly and cost-
    effectively than other methods. Sound, speech and music Generative
    models can synthesize natural-sounding speech and audio content
    for voice-enabled AI chatbots and digital assistants, audiobook
    narration and other applications. The same technology can generate
    original music that mimics the structure and sound of professional
    compositions. Software code Gen AI can generate original code,
    autocomplete code snippets, translate between programming
    languages and summarize code functionality. It enables developers
    to quickly prototype, refactor, and debug applications while
    offering a natural language interface for coding tasks. Design and
    art Generative AI models can generate unique works of art and
    design, or assist in graphic design. Applications include dynamic
    generation of environments, characters or avatars, and special
    effects for virtual simulations and video games. Simulations and
    synthetic data Generative AI models can be trained to generate
    synthetic data , or synthetic structures based on real or
    synthetic data. For example, generative AI is applied in drug
    discovery to generate molecular structures with desired
    properties, aiding in the design of new pharmaceutical compounds.
    Industry newsletter The latest AI trends, brought to you by
    experts Get curated insights on the most important—and
    intriguing—AI news. Subscribe to our weekly Think newsletter. See
    the IBM Privacy Statement . Thank you! You are subscribed. Your
    subscription will be delivered in English. You will find an
    unsubscribe link in every newsletter. You can manage your
    subscriptions or unsubscribe here . Refer to our IBM Privacy
    Statement for more informa

------------------------------------------------------------


---------- ✨ RESULT #2 ✨ ----------------------------------------

  📌 Title: Generative artificial intelligence - Wikipedia
  🌐 URL  : https://en.wikipedia.org/wiki/Generative_artificial_intelligence

  📊 Detailed Analysis (General Web Page):
    - Url: https://en.wikipedia.org/wiki/Generative_artificial_intelligence
    - Title: Generative artificial intelligence - Wikipedia
    - Meta Description: No Meta Description
    - Main Heading: Generative artificial intelligence
    - Summary Text:  Generative artificial intelligence(Generative AI,GenAI,[1]orGAI) is a subfield ofartificial intelligencethat usesgenerative modelsto produce text, images, videos, or other forms of data.[2][3][4]These modelslearnthe underlying patterns and structures of theirtraining dataand use them to produce new data[5][6]based on the input, which often comes in the form of natural languageprompts.[7][8] Generative AI tools have become more common since theAI boomin the 2020s. This boom was made possible by improvements intransformer-baseddeepneural networks, particularlylarge language models(LLMs). Major tools includechatbotssuch asChatGPT,Copilot,Gemini,Claude,Grok, andDeepSeek;text-to-imagemodels such asStable Diffusion,Midjourney, andDALL-E; andtext-to-videomodels such asVeoandSora.[9][10][11][12]Technology companies developing generative AI includeOpenAI,Anthropic,Meta AI,Microsoft,Google,DeepSeek, andBaidu.[7][13][14] Generative AI has raised many ethical questions as it can be used forcyb...
    - Links: (Complex Data - See raw content)
    - Keywords: description, artificial, wikipedia, meta, generative, intelligence
    - Author: Contributors to Wikimedia projects
    - Published Date: Not specified
    - Structured Data: (Complex Data - See raw content)

  📄 Raw Content Excerpt:
    Generative artificial intelligence - Wikipedia Jump to content
    From Wikipedia, the free encyclopedia Subset of AI using
    generative models Not to be confused with Artificial general
    intelligence . Théâtre D'opéra Spatial (2022), an image made using
    generative AI Part of a series on Artificial intelligence (AI)
    Major goals Artificial general intelligence Intelligent agent
    Recursive self-improvement Planning Computer vision General game
    playing Knowledge representation Natural language processing
    Robotics AI safety Approaches Machine learning Symbolic Deep
    learning Bayesian networks Evolutionary algorithms Hybrid
    intelligent systems Systems integration Applications
    Bioinformatics Deepfake Earth sciences Finance Generative AI Art
    Audio Music Government Healthcare Mental health Industry Software
    development Translation Military Physics Projects Philosophy
    Artificial consciousness Chinese room Friendly AI Control problem
    / Takeover Ethics Existential risk Turing test Uncanny valley
    History Timeline Progress AI winter AI boom Glossary Glossary v t
    e Generative artificial intelligence ( Generative AI , GenAI , [ 1
    ] or GAI ) is a subfield of artificial intelligence that uses
    generative models to produce text, images, videos, or other forms
    of data. [ 2 ] [ 3 ] [ 4 ] These models learn the underlying
    patterns and structures of their training data and use them to
    produce new data [ 5 ] [ 6 ] based on the input, which often comes
    in the form of natural language prompts . [ 7 ] [ 8 ] Generative
    AI tools have become more common since the AI boom in the 2020s.
    This boom was made possible by improvements in transformer -based
    deep neural networks , particularly large language models (LLMs).
    Major tools include chatbots such as ChatGPT , Copilot , Gemini ,
    Claude , Grok , and DeepSeek ; text-to-image models such as Stable
    Diffusion , Midjourney , and DALL-E ; and text-to-video models
    such as Veo and Sora . [ 9 ] [ 10 ] [ 11 ] [ 12 ] Technology
    companies developing generative AI include OpenAI , Anthropic ,
    Meta AI , Microsoft , Google , DeepSeek , and Baidu . [ 7 ] [ 13 ]
    [ 14 ] Generative AI has raised many ethical questions as it can
    be used for cybercrime , or to deceive or manipulate people
    through fake news or deepfakes . [ 15 ] Even if used ethically, it
    may lead to mass replacement of human jobs . [ 16 ] The tools
    themselves have been criticized as violating intellectual property
    laws, since they are trained on copyrighted works. [ 17 ]
    Generative AI is used across many industries. Examples include
    software development, [ 18 ] healthcare, [ 19 ] finance, [ 20 ]
    entertainment, [ 21 ] customer service, [ 22 ] sales and
    marketing, [ 23 ] art, writing, [ 24 ] fashion, [ 25 ] and product
    design. [ 26 ] History [ edit ] Main article: History of
    artificial intelligence Early history [ edit ] The first example
    of an algorithmically generated media is likely the Markov chain .
    Markov chains have long been used to model natural languages since
    their development by Russian mathematician Andrey Markov in the
    early 20th century. Markov published his first paper on the topic
    in 1906, [ 27 ] [ 28 ] and analyzed the pattern of vowels and
    consonants in the novel Eugeny Onegin using Markov chains. Once a
    Markov chain is trained on a text corpus , it can then be used as
    a probabilistic text generator. [ 29 ] [ 30 ] Computers were
    needed to go beyond Markov chains. By the early 1970s, Harold
    Cohen was creating and exhibiting generative AI works created by
    AARON , the computer program Cohen created to generate paintings.
    [ 31 ] The terms generative AI planning or generative planning
    were used in the 1980s and 1990s to refer to AI planning systems,
    especially computer-aided process planning , used to generate
    sequences of actions to reach a specified goal. [ 32 ] [ 33 ]
    Generative AI planning systems used symbolic AI methods such as
    state space search and constraint satisfaction and were a
    "relatively mature" technology by the early 1990s. They were used
    to generate crisis action plans for military use, [ 34 ] process
    plans for manufacturing [ 32 ] and decision plans such as in
    prototype autonomous spacecraft. [ 35 ] Generative neural networks
    (2014–2019) [ edit ] See also: Machine learning and deep learning
    Above: An image classifier , an example of a neural network
    trained with a discriminative objective. Below: A text-to-image
    model , an example of a network trained with a generative
    objective. Since inception, the field of machine learning has used
    both discriminative models and generative models to model and
    predict data. Beginning in the late 2000s, the emergence of deep
    learning drove progress, and research in image classification ,
    speech recognition , natural language processing and other tasks.
    Neural networks in this era were typically trained as
    discriminative models due to the difficulty of generative
    modeling. [ 36 ] In 2014, advancements such as the variational
    autoencoder and generative adversarial network produced the first
    practical deep neural networks capable of learning generative
    models, as opposed to discriminative ones, for complex data such
    as images. These deep generative models were the first to output
    not only class labels for images but also entire images. In 2017,
    the Transformer network enabled advancements in generative models
    compared to older Long-Short Term Memory models, [ 37 ] leading to
    the first generative pre-trained transformer (GPT), known as GPT-1
    , in 2018. [ 38 ] This was followed in 2019 by GPT-2 , which
    demonstrated the ability to generalize unsupervised to many
    different tasks as a Foundation model . [ 39 ] The new generative
    models introduced during this period allowed for large neural
    networks to be trained using unsupervised learning or semi-
    supervised learning , rather than the supervised learning typical
    of discriminative models. Unsupervised learning removed the need
    for humans to manually label data , allowing for larger networks
    to be trained. [ 40 ] Generative AI boom (2020–) [ edit ] Main
    article: AI boom AI generated images have become much more
    advanced. In March 2020, the release of 15.ai , a free web
    application created by an anonymous MIT researcher that could
    generate convincing character voices using minimal training data,
    marked one of the earliest popular use cases of generative AI. [
    41 ] The platform is credited as the first mainstream service to
    popularize AI voice cloning ( audio deepfakes ) in memes and
    content creation , influencing subsequent developments in voice AI
    technology . [ 42 ] [ 43 ] In 2021, the emergence of DALL-E , a
    transformer -based pixel generative model, marked an advance in
    AI-generated imagery. [ 44 ] This was followed by the releases of
    Midjourney and Stable Diffusion in 2022, which further
    democratized access to high-quality artificial intelligence art
    creation from natural language prompts . [ 45 ] These systems
    demonstrated unprecedented capabilities in generating
    photorealistic images, artwork, and designs based on text
    descriptions, leading to widespread adoption among artists,
    designers, and the general public. In late 2022, the public
    release of ChatGPT revolutionized the accessibility and
    application of generative AI for general-purpose text-based tasks.
    [ 46 ] The system's ability to engage in natural conversations ,
    generate creative content , assist with coding, and perform
    various analytical tasks captured global attention and sparked
    widespread discussion about AI's potential impact on work ,
    education , and creativity . [ 47 ] In March 2023, GPT-4 's
    release represented another jump in generative AI capabilities. A
    team from Microsoft Research controversially argued that it "could
    reasonably be viewed as an early (yet still incomplete) version of
    an artificial general intelligence (AGI) system." [ 48 ] However,
    this assessment was contested by other scholars who maintained
    that generative AI remained "still far from reaching the benchmark
    of 'general human intelligence'" as of 2023. [ 49 ] Later in 2023,
    Meta released ImageBind , an AI model combining multiple
    modalities including text, images, video, thermal data, 3D data,
    audio, and motion, paving the way for more immersive generative AI
    applications. [ 50 ] In December 2023, Google unveiled Gemini , a
    multimodal AI model available in four versions: Ultra, Pro, Flash,
    and Nano. [ 51 ] The company integrated Gemini Pro into its Bard
    chatbot and announced plans for "Bard Advanced" powered by the
    larger Gemini Ultra model. [ 52 ] In February 2024, Google unified
    Bard and Duet AI under the Gemini brand, launching a mobile app on
    Android and integrating the service into the Google app on iOS . [
    53 ] In March 2024, Anthropic released the Claude 3 family of
    large language models, including Claude 3 Haiku, Sonnet, and Opus.
    [ 54 ] The models demonstrated significant improvements in
    capabilities across various benchmarks, with Claude 3 Opus notably
    outperforming leading models from OpenAI and Google. [ 55 ] In
    June 2024, Anthropic released Claude 3.5 Sonnet, which
    demonstrated improved performance compared to the larger Claude 3
    Opus, particularly in areas such as coding, multistep workflows,
    and image analysis. [ 56 ] Private investment in AI (pink) and
    generative AI (green). Asia–Pacific countries are significantly
    more optimistic than Western societies about generative AI and
    show higher adoption rates. Despite expressing concerns about
    privacy and the pace of change, in a 2024 survey, 68% of Asia-
    Pacific respondents believed that AI was having a positive impact
    on the world, compared to 57% globally. [ 57 ] According to a
    survey by SAS and Coleman Parkes Research, China in particular has
    emerged as a global leader in generative AI adoption, with 83% of
    Chinese respondents using the technology, exceeding both the
    global average of 54% and the U.S. rate of 65%. This leadership is
    further evidenced by China's intellectual property developments in
    the field, with a UN report revealing that Chinese entities filed
    over 38,000 generative AI patents from 2014 to 2023, substantially
    surpassing the United States in patent applications. [ 58 ] A 2024
    survey on the Chinese social app Soul reported that 18% of
    respondents born after 2000 used generative AI "almost every day",
    and that over 60% of respondents like or love AI-generated
    content, while less than 3% dislike or hate it. [ 59 ]
    Applications [ edit ] Notable types of generative AI models
    include generative pre-trained transformers (GPTs), generative
    adversarial networks (GANs), and variational autoencoders (VAEs).
    Generative AI systems are multimodal if they can process multiple
    types of inputs or generate multiple types of outputs. [ 60 ] For
    example, GPT-4o can both process and generate text, images and
    audio. [ 61 ] Generative AI has made its appearance in a wide
    variety of industries, radically changing the dynamics of content
    creation, analysis, and delivery. In healthcare, [ 62 ] generative
    AI is instrumental in accelerating drug discovery by creating
    molecular structures with target characteristics [ 63 ] and
    generating radiology images for training diagnostic models. This
    extraordinary ability not only enables faster and cheaper
    development but also enhances medical decision-making. In finance,
    generative AI is invaluable as it generates datasets to train
    models and automates report generation with natural language
    summarization capabilities. It automates content creation,
    produces synthetic financial data, and tailors customer
    communications. It also powers chatbots and virtual agents.
    Collectively, these technologies enhance efficiency, reduce
    operational costs, and support data-driven decision-making in
    financial institutions. [ 64 ] The media industry makes use of
    generative AI for numerous creative activities such as music
    composition, scriptwriting, video editing, and digital art. The
    educational sector is impacted as well, since the tools make
    learning personalized through creating quizzes, study aids, and
    essay composition. Both the teachers and the learners benefit from
    AI-based platforms that suit various learning patterns. [ 65 ]
    Text and software code [ edit ] Main article: Large language model
    See also: Code completion , Autocomplete , and Vibe coding Jung
    believed that the shadow self is not entirely evil or bad, but
    rather a potential source of creativity and growth. He argued that
    by embracing, rather than ignoring, our shadow self, we can
    achieve a deeper understand

------------------------------------------------------------


---------- ✨ RESULT #3 ✨ ----------------------------------------

  📌 Title: What is Generative AI? - GeeksforGeeks
  🌐 URL  : https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/

  📊 Detailed Analysis (General Web Page):
    - Url: https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/
    - Title: What is Generative AI? - GeeksforGeeks
    - Meta Description: Your All-in-One Learning Portal: GeeksforGeeks is a comprehensive educational platform that empowers learners across domains-spanning computer science and programming, school education, upskilling, commerce, software tools, competitive exams, and more.
    - Main Heading: What is Generative AI?
    - Summary Text: Generative artificial intelligence, often called generative AI or gen AI, is a type of AI that can create new content like conversations, stories, images, videos, and music. It can learn about different topics such as languages, programming, art, science, and more, and use this knowledge to solve new problems. For example: It can learn about popular design styles and create a unique logo for a brand or an organisation. Businesses can use generative AI in many ways, like building chatbots, creating media, designing products, and coming up with new ideas. Generative AI has come a long way from its early beginnings. Here's how it has evolved over time, step by step: Generative AI is versatile, with different models designed for specific tasks. Here are some types:
    - Links: (Complex Data - See raw content)
    - Keywords: Generative AI, machine learning, deep learning, Generative Adversarial Networks, Large Language Models, multimodal generative AI, text-to-image generation, image-to-image transformation, speech-to-text technology, text-to-video models, creative content generation, personalized marketing campaigns, ethical concerns in AI, AI-powered design tools
    - Author: GeeksforGeeks
    - Published Date: 2023-08-16 12:11:46+00:00
    - Structured Data: (Complex Data - See raw content)

  📄 Raw Content Excerpt:
    What is Generative AI? - GeeksforGeeks Data Science Data Science
    Projects Data Analysis Data Visualization Machine Learning ML
    Projects Deep Learning NLP Computer Vision Artificial Intelligence
    Open In App Next Article: Generative Adversarial Network (GAN)
    What is Generative AI? Last Updated : 23 Jan, 2025 Summarize
    Comments Improve Suggest changes Share Like Article Like Report
    Generative artificial intelligence, often called generative AI or
    gen AI, is a type of AI that can create new content like
    conversations, stories, images, videos, and music. It can learn
    about different topics such as languages, programming, art,
    science, and more, and use this knowledge to solve new problems.
    For example: It can learn about popular design styles and create a
    unique logo for a brand or an organisation. Businesses can use
    generative AI in many ways, like building chatbots, creating
    media, designing products, and coming up with new ideas. Evolution
    of Generative AI Generative AI has come a long way from its early
    beginnings. Here's how it has evolved over time, step by step: 1.
    The Early Days: Rule-Based Systems AI systems followed strict
    rules written by humans to produce results. These systems could
    only do what they were programmed for and couldn't learn or adapt.
    For example, a program could create simple shapes but couldn’t
    draw something creative like a landscape. 2. Introduction of
    Machine Learning (1990s-2000s) AI started using machine learning,
    which allowed it to learn from data instead of just following
    rules. The AI was fed large datasets (e.g., pictures of animals),
    and it learned to identify patterns and make predictions. Example:
    AI could now recognize a dog in a picture, but it still couldn’t
    create a picture of a dog on its own. 3. The Rise of Deep Learning
    (2010s) Deep learning improved AI significantly by using neural
    networks, which mimic how the human brain works. AI could now
    process much more complex data, like thousands of photos, and
    start generating new content. Example: AI could now create a
    realistic drawing of a dog by learning from millions of dog
    photos. 4. Generative Adversarial Networks (2014) GANs, introduced
    in 2014, use two AI systems that work together: one generates new
    content, and the other checks if it looks real. This made
    generative AI much better at creating realistic images, videos,
    and sounds. Example: GANs can create life like images of people
    who don’t exist or filters (used in apps like FaceApp or Snapchat
    ). 5. Large Language Models (LLMs) and Beyond (2020s) Models like
    GPT-3 and GPT-4 can understand and generate human-like text. They
    are trained on massive amounts of data from books, websites, and
    other sources. AI can now hold conversations, write essays,
    generate code, and much more. Example: ChatGPT can help you draft
    an email, write a poem, or even solve problems. 6. Multimodal
    Generative AI (Present) New AI models can handle multiple types of
    data at once—text, images, audio, and video. This allows AI to
    create content that combines different formats. Example: AI can
    take a written description and turn it into an animated video or a
    song with the help of different models integrating together. Types
    of Generative AI Models Generative AI is versatile, with different
    models designed for specific tasks. Here are some types: Text-to-
    Text : These models generate meaningful and coherent text based on
    input text. They are widely used for tasks like drafting emails,
    summarizing lengthy documents, translating languages, or even
    writing creative content. Tools like ChatGPT is brilliant at
    understanding context and producing human-like responses. Text-to-
    Image : This involves generating realistic images from descriptive
    text. For Example, tools like DALL-E 2 can create a custom digital
    image based on prompts such as "A peaceful beach with palm trees
    during a beautiful sunset," offering endless possibilities for
    designers, artists, and marketers. Image-to-Image : These models
    enhance or transform images based on input image . For example,
    they can convert a daytime photo into a night time scene, apply
    artistic filters, or refine low-resolution images into high-
    quality visuals. Image-to-Text : AI tools analyze and describe the
    content of images in text form. This technology is especially
    beneficial for accessibility, helping visually impaired
    individuals understand visual content through detailed captions.
    Speech-to-Text : This application converts spoken words into
    written text. It powers virtual assistants like Siri,
    transcription software, and automated subtitles, making it a vital
    tool for communication, accessibility, and documentation. Text-to-
    Audio : Generative AI can create music, sound effects, or audio
    narrations from textual prompts. This empowers creators to explore
    new soundscapes and compose unique auditory experiences tailored
    to specific themes or moods. Text-to-Video : These models allow
    users to generate video content by describing their ideas in text.
    For example, a marketer could input a vision for a promotional
    video, and the AI generates visuals and animations, streamlining
    content creation. Multimodal AI : These systems integrate multiple
    input and output formats, like text, images, and audio, into a
    unified interface. For instance, an educational platform could let
    students ask questions via text and receive answers as interactive
    visuals or audio explanations, enhancing learning experiences.
    Relationship Between Humans and Generative AI In today’s world,
    Generative AI has become a trusted best friend for humans, working
    alongside us to achieve incredible things. Imagine a painter
    creating a masterpiece, while they focus on the vision, Generative
    AI acts as their assistant, mixing colors, suggesting designs, or
    even sketching ideas. The painter remains in control, but the AI
    makes the process faster and more exciting. This partnership is
    like having a friend who’s always ready to help. A writer stuck on
    the opening line of a story can turn to Generative AI for
    suggestions that spark creativity. A business owner without design
    skills can rely on AI to draft a sleek website or marketing
    materials. Even students can use AI to better understand complex
    topics by generating easy-to-grasp explanations or visual aids.
    Generative AI is not here to replace humans but to empower them.
    It takes on repetitive tasks, offers endless possibilities, and
    helps people achieve results they might not have imagined alone.
    At the same time, humans bring their intuition, creativity, and
    ethical judgment, ensuring the AI’s contributions are meaningful
    and responsible. In this era, Generative AI truly feels like a
    best friend—always there to support, enhance, and inspire us while
    letting us stay in charge. Together, humans and AI make an
    unbeatable team, achieving more than ever before. Generative AI Vs
    AI Criteria Generative AI Artificial Intelligence Purpose It is
    designed to produce new content or data Designed for a wide range
    of tasks but not limited to generation Application Art creation,
    text generation, video synthesis, and so on Data analysis,
    predictions, automation, robotics, etc Learning Uses Unsupervised
    learning or reinforcement learning Can use supervised, semi-
    supervised, or reinforcement Outcome New or original output is
    created Can produce an answer and make a decision, classify, data,
    etc. Complexity It requires a complex model like GANs It has
    ranged from simple linear regression to complex neural networks
    Data Requirement Required a large amount of data to produce
    results of high-quality data Data requirements may vary; some need
    little data, and some need vast amounts Interactivity Can be
    interactive, responding to user input Might not always be
    interactive, depending on the application Benefits of Generative
    AI Generative AI offers innovative tools that enhance creativity,
    efficiency, and personalization across various fields. Enhances
    Creativity : Generative AI enables the creation of original
    content like images, music, and text, helping artists, designers,
    and writers explore fresh ideas. It bridges the gap between human
    creativity and machine-generated innovation, making the creative
    process more dynamic. Accelerates Research and Development : In
    fields like science and technology, Generative AI reduces the time
    needed for research by generating multiple outcomes and
    predictions, such as molecular structures in drug development.
    This speeds up innovation and helps solve complex problems
    efficiently. Improves Personalization : Generative AI creates
    tailored content based on user preferences. From personalized
    product designs to customized marketing campaigns, it enhances
    user engagement and satisfaction by delivering exactly what users
    need or want. Empowers Non-Experts : Even users without expertise
    can create high-quality content using Generative AI. This helps
    individuals learn new skills, access creative tools, and open
    doors to personal and professional growth. Drives Economic Growth
    : Generative AI introduces new roles and opportunities by
    fostering innovation, automating tasks, and enhancing
    productivity. This leads to economic expansion and the creation of
    jobs in emerging fields. Limitations of Generative AI While
    Generative AI offers many benefits, it also comes with certain
    limitations that need to be addressed Data Dependence : The
    accuracy and quality of Generative AI outputs depend entirely on
    the data it is trained on. If the training data is biased,
    incomplete, or inaccurate, the generated content will reflect
    these flaws. Limited Control Over Outputs : Generative AI can
    produce unexpected or irrelevant results, making it challenging to
    control the content and ensure it aligns with specific user
    requirements. High Computational Requirements : Training and
    running Generative AI models demand significant computing power,
    which can be costly and resource-intensive. This limits
    accessibility for smaller organizations or individuals. Ethical
    and Legal Concerns : Generative AI can be misused to create
    harmful content, like deepfakes or fake news, which can spread
    misinformation or violate privacy. These ethical and legal
    challenges require careful regulation and oversight to prevent
    abuse. Q1. Is generative AI replacing jobs? Generative AI isn’t
    about replacing jobs but transforming them. It automates
    repetitive tasks, allowing people to focus on more creative and
    strategic aspects of their work. For example, content writers can
    use AI for inspiration or to speed up first drafts, while
    designers can use it to generate quick mockups. Q2. How does
    Generative AI work? Generative AI works by teaching computer
    programs (like GPT-3 or GANs) from lots of examples. These
    programs learn how things are usually done from the data they
    study. Then, they can use this knowledge to create new stuff when
    given a starting point or a request. Q3. What are common use cases
    for Generative AI? Generative AI has a wide range of applications,
    including content generation, language translation, chatbots,
    image and video creation, data augmentation, and personalized
    marketing. It can also be used in artistic creation, medical image
    generation, and more. Q4. Is Generative AI different from other AI
    types? Yes, Generative AI is different from other AI types, like
    classification or regression models. While those models make
    predictions or classify data, generative models focus on creating
    new, original data based on the patterns they’ve learned. They are
    versatile and used for creative tasks. Q5. How can I get started
    with generative AI? You can start by exploring tools and platforms
    like ChatGPT for text generation, DALL-E for image generation, or
    similar tools for your needs. Many platforms also provide APIs,
    allowing developers to integrate AI capabilities into their own
    applications. Learning basic prompt engineering can also help you
    get the most out of these tools. Next Article Generative
    Adversarial Network (GAN) A anushka_jain_gfg Improve Article Tags
    : Artificial Intelligence AI-ML-DS Generative AI Similar Reads
    Artificial Intelligence Tutorial | AI Tutorial Artificial
    Intelligence (AI) refers to the simulation of human intelligence
    in machines which helps in allowing them to think and act like
    humans. It involves creating algorithms and systems that can
    perform tasks which requiring human abilities such as visual
    perception, speech recognition, decisio 5 min read Introduction to
    AI What is Artificial I

------------------------------------------------------------


======================================================================
                   ✨ Scraping Process Completed ✨
======================================================================
```
</details>

## Cloudflare Worker Version

A serverless scraper implemented as a Cloudflare Worker that leverages Jina AI for search and Groq LLM for content analysis. Rotate multiple API keys via GetPantry.

See `Cloudflare worker based jina ai & groq scraper/README.md` for full details.

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`
- `lxml`

## License

MIT License

