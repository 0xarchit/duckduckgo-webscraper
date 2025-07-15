# === standalone working version ===

import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urlparse, parse_qs, unquote, urljoin, quote_plus
import json
import textwrap

proxy_list = []
proxy_index = 0
cached_proxy = None

def print_banner():
    print("\n" + "="*70)
    print("                     🌐 DuckDuckGo Query Scraper 🌐")
    print("                            By 0xArchit")
    print("="*70 + "\n")

def fetch_proxies():
    global proxy_list, proxy_index
    # source: https://github.com/search?q=proxy+list&type=repositories&s=updated&o=desc
    # url = "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/https.txt"
    # url = "https://raw.githubusercontent.com/theriturajps/proxy-list/refs/heads/main/proxies.txt"
    # url = "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt"
    # url = "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/refs/heads/main/proxies/https.txt"
    # url = "https://raw.githubusercontent.com/fyvri/fresh-proxy-list/archive/storage/classic/https.txt"
    # url = "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt"
    # url = "https://raw.githubusercontent.com/SoliSpirit/proxy-list/refs/heads/main/https.txt"
    # url = "https://raw.githubusercontent.com/databay-labs/free-proxy-list/refs/heads/master/https.txt"
    url = "https://raw.githubusercontent.com/0xarchit/duckduckgo-webscraper/refs/heads/main/proxies.txt"
    # === Credits To Original Proxy Providers ===
    try:
        print("🚀 Fetching fresh proxy list...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        proxy_list = response.text.strip().split('\n')
        proxy_index = 0
        print(f"✅ Loaded {len(proxy_list)} proxies.")
    except Exception as e:
        print(f"❌ Failed to load proxy list: {e}. Proceeding without proxies (may be blocked)." )
        proxy_list = []

def get_next_working_proxy():
    global proxy_list, proxy_index, cached_proxy

    if not proxy_list:
        raise Exception("No proxies available to test.")

    initial_proxy_index = proxy_index
    proxies_tried_in_this_cycle = 0

    while proxies_tried_in_this_cycle < len(proxy_list):
        proxy = proxy_list[proxy_index]
        proxy_index = (proxy_index + 1) % len(proxy_list)
        proxies_tried_in_this_cycle += 1

        proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        print(f"🔌 Testing proxy: {proxy}")
        try:
            response = requests.get("https://httpbin.org/ip", proxies=proxy_dict, timeout=10)
            if response.status_code == 200:
                cached_proxy = proxy_dict
                print(f"✅ Proxy working: {proxy}")
                return proxy_dict
        except requests.exceptions.RequestException as e:
            print(f"    Proxy test failed for {proxy}: {e}")
            pass
        time.sleep(1)

    raise Exception("No working proxy found after cycling through available proxies.")

def extract_clean_text(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside', 'form', 'img', 'noscript', 'iframe', 'button', 'input', 'select', 'textarea']):
        tag.decompose()
    
    text = soup.get_text(separator='\n').strip()
    text = re.sub(r'[\n\s]+', ' ', text)
    return text

def parse_general_content(url, html_content):
    """
    Parses the HTML content of a general web page to extract structured data.

    This enhanced function improves upon the original by:
    - Adopting a more resilient and comprehensive fallback strategy for essential data points like title, description, and headings.
    - Extracting structured data (JSON-LD) for more precise information.
    - Implementing a more intelligent content extraction method that prioritizes main content articles.
    - Broadening the scope of link extraction to include internal, external, and social media links.
    - Improving contact information retrieval by searching for mailto links.
    - Adding extraction for author and publication date information.
    """
    soup = BeautifulSoup(html_content, "lxml")
    data = {"type": "General Web Page", "url": url}

    # 1. Enhanced Title Extraction
    title_tag = soup.find('title')
    og_title = soup.find('meta', property='og:title')
    twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
    meta_title = soup.find('meta', attrs={'name': 'title'})
    
    title_candidates = [
        title_tag.get_text(strip=True) if title_tag else None,
        og_title['content'].strip() if og_title and og_title.get('content') else None,
        twitter_title['content'].strip() if twitter_title and twitter_title.get('content') else None,
        meta_title['content'].strip() if meta_title and meta_title.get('content') else None
    ]
    data['title'] = next((title for title in title_candidates if title), "No Title Found")

    # 2. Comprehensive Meta Description
    og_desc = soup.find('meta', property='og:description')
    twitter_desc = soup.find('meta', attrs={'name': 'twitter:description'})
    meta_desc = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', itemprop='description')

    description_candidates = [
        og_desc['content'].strip() if og_desc and og_desc.get('content') else None,
        twitter_desc['content'].strip() if twitter_desc and twitter_desc.get('content') else None,
        meta_desc['content'].strip() if meta_desc and meta_desc.get('content') else None
    ]
    data['meta_description'] = next((desc for desc in description_candidates if desc), "No Meta Description")

    # 3. Main Heading (h1) with Fallback to Title
    h1 = soup.find('h1')
    data['main_heading'] = h1.get_text(strip=True) if h1 else data.get('title', 'No Main Heading')

    # 4. Intelligent Content Summary from Main Article
    main_content = soup.find('article') or soup.find('main') or soup
    paragraphs = main_content.find_all('p', limit=5)
    if paragraphs:
        body_text = ' '.join(p.get_text(strip=True) for p in paragraphs)
        data['summary_text'] = (body_text[:997] + '...') if len(body_text) > 1000 else body_text
    else:
        data['summary_text'] = "No significant paragraph text found."

    # 5. Categorized Link Extraction
    links = {'internal': [], 'external': [], 'social': []}
    social_domains = ['facebook.com', 'twitter.com', 'linkedin.com', 'instagram.com']
    for link_tag in soup.find_all('a', href=True):
        href = link_tag['href']
        text = link_tag.get_text(strip=True)
        if not text:
            continue

        if any(domain in href for domain in social_domains):
            if len(links['social']) < 5:
                links['social'].append({"text": text, "href": href})
        elif href.startswith('http'):
            if len(links['external']) < 10:
                links['external'].append({"text": text, "href": urljoin(url, href)})
        elif not href.startswith('#'):
            if len(links['internal']) < 10:
                links['internal'].append({"text": text, "href": urljoin(url, href)})
    data['links'] = links

    # 6. Improved Contact Info Extraction
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', html_content)
    if email_match:
        data['email'] = email_match.group(0)
    else:
        mailto_link = soup.select_one('a[href^="mailto:"]')
        if mailto_link:
            data['email'] = mailto_link['href'][7:]

    # 7. Comprehensive Keyword Extraction
    meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
    if meta_keywords and meta_keywords.get('content'):
        data['keywords'] = [kw.strip() for kw in meta_keywords['content'].split(',') if kw.strip()]
    else:
        text_for_keywords = data.get('title', '') + ' ' + data.get('meta_description', '')
        words = re.findall(r'\b\w{4,}\b', text_for_keywords.lower())
        if len(words) > 3:
             data['keywords'] = list(set(words))[:10] # Get unique words
        else:
            data['keywords'] = "No keywords found."

    # 8. Author and Publication Date
    author_meta = soup.find('meta', attrs={'name': 'author'})
    data['author'] = author_meta['content'].strip() if author_meta and author_meta.get('content') else 'Not specified'
    
    pub_date_meta = soup.find('meta', property='article:published_time') or soup.find('time', {'itemprop': 'datePublished'})
    data['published_date'] = pub_date_meta['datetime' if pub_date_meta.has_attr('datetime') else 'content'] if pub_date_meta else 'Not specified'

    # 9. JSON-LD Structured Data Extraction
    json_ld_scripts = soup.find_all('script', type='application/ld+json')
    for script in json_ld_scripts:
        try:
            json_data = json.loads(script.string)
            if isinstance(json_data, list):
                if 'structured_data' not in data:
                    data['structured_data'] = {}
                for item in json_data:
                    data['structured_data'].update(item)
            else:
                data['structured_data'] = json_data
            # Process author in structured_data safely
            author_meta = data.get('structured_data', {}).get('author')
            if author_meta:
                if isinstance(author_meta, list) and author_meta:
                    first = author_meta[0]
                    if isinstance(first, dict):
                        data['author'] = first.get('name', data['author'])
                elif isinstance(author_meta, dict):
                    data['author'] = author_meta.get('name', data['author'])

        except json.JSONDecodeError:
            continue

    return data


def scrape_with_cached_proxy(url, max_attempts_per_url=5):
    global cached_proxy
    current_attempt = 0
    
    while current_attempt < max_attempts_per_url:
        proxy_to_use = cached_proxy
        if not proxy_to_use:
            try:
                proxy_to_use = get_next_working_proxy()
            except Exception as e:
                print(f"🛑 Error getting new proxy for {url}: {e}. Giving up on this URL.")
                break 

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

        try:
            print(f"🌐 Attempt {current_attempt + 1}/{max_attempts_per_url} Scraping: {url} with proxy: {proxy_to_use['http']}")
            response = requests.get(url, headers=headers, proxies=proxy_to_use, timeout=15)
            if response.status_code == 200:
                print(f"  ✅ Successfully scraped {url}")
                return response.content
            else:
                print(f"  ⚠️ Received status code {response.status_code} for {url}. Attempting new proxy.")
                cached_proxy = None
        except requests.exceptions.RequestException as e:
            print(f"  ⚠️ Proxy failed for {url} (Attempt {current_attempt + 1}): {e}. Attempting new proxy.")
            cached_proxy = None

        current_attempt += 1
        time.sleep(2)

    print(f"❌ Failed to scrape {url} after {max_attempts_per_url} proxy attempts. Skipping this URL.")
    return None

def duckduckgo_search(query, max_results=3):
    encoded_query = quote_plus(query)
    search_url = f"https://lite.duckduckgo.com/lite/?q={encoded_query}"
    print(f"\n🔍 Initiating DuckDuckGo Lite search for: '{query}'")
    html = scrape_with_cached_proxy(search_url)

    if html is None:
        raise Exception("Failed to get search results from DuckDuckGo itself. Please check your connection or proxies.")

    print("⏳ Waiting 5 seconds after DuckDuckGo search to avoid rate limits...")
    time.sleep(5)

    soup = BeautifulSoup(html, "html.parser")
    results = []

    for a in soup.select("a.result-link"):
        if len(results) >= max_results:
            break
        title = a.get_text(strip=True)
        raw_link = a['href']
        # Skip ad redirect JS URLs and help pages
        if 'y.js' in raw_link or 'duckduckgo-help-pages' in raw_link:
            print(f"🚫 Skipping ad/help link: {raw_link}")
            continue
        # Decode DuckDuckGo redirect link (uddg)
        if "duckduckgo.com/l/?" in raw_link and "uddg=" in raw_link:
            try:
                parsed = urlparse(raw_link)
                query_params = parse_qs(parsed.query)
                real_url = unquote(query_params.get('uddg', [''])[0])
                if real_url.startswith("//"):
                    real_url = "https:" + real_url
            except Exception as e:
                print(f"⚠️ Error decoding DuckDuckGo URL {raw_link}: {e}")
                real_url = raw_link
        else:
            real_url = raw_link
        print(f"\n➡️ Found result: '{title}'\n   🔗 Link: {real_url}")
        print("⏳ Waiting 5 seconds before scraping this result page...")
        time.sleep(5)
        page_html = scrape_with_cached_proxy(real_url, max_attempts_per_url=5)
        if not page_html:
            print(f"🚫 Skipping {real_url} due to repeated proxy failures.")
            continue
        html_string = page_html.decode('utf-8', 'ignore')
        structured_content = parse_general_content(real_url, html_string)
        page_text = extract_clean_text(html_string)
        results.append({
            "title": title,
            "url": real_url,
            "raw_content_excerpt": page_text[:25000] + ("..." if len(page_text) > 25000 else ""),
            "structured_content": structured_content
        })

    return results

def print_formatted_results(results):
    print("\n" + "="*20 + " UNIVERSAL SCRAPE REPORT " + "="*20 + "\n")
    if not results:
        print("😔 No results found or all failed to load for your query.")
        return

    for i, res in enumerate(results, 1):
        print(f"\n{'-'*10} ✨ RESULT #{i} ✨ {'-'*40}\n")
        print(f"  📌 Title: \033[1m{res['title']}\033[0m")
        print(f"  🌐 URL  : \033[4m{res['url']}\033[0m\n")

        structured_data = res['structured_content']
        print(f"  📊 Detailed Analysis ({structured_data.get('type', 'Unknown')}):")

        for key, value in structured_data.items():
            if key == 'type':
                continue

            formatted_key = key.replace('_', ' ').title()

            if isinstance(value, list):
                if value and isinstance(value[0], dict):
                    print(f"    - {formatted_key}:")
                    if not value:
                        print(f"      (None)")
                    else:
                        for item in value:
                            print(f"      • {item.get('text', 'N/A')}: {item.get('href', 'N/A')}")
                else:
                    print(f"    - {formatted_key}: {', '.join(value) if value else '(None)'}")
            elif isinstance(value, dict):
                print(f"    - {formatted_key}: (Complex Data - See raw content)")
            else:
                print(f"    - {formatted_key}: {value if value else '(Not found)'}")
        
        print("\n  📄 Raw Content Excerpt:")
        excerpt = res['raw_content_excerpt']
        if excerpt and excerpt != "[Failed to load page content after multiple attempts]":
            wrapped_excerpt = textwrap.fill(excerpt, width=70, initial_indent="    ", subsequent_indent="    ")
            print(wrapped_excerpt)
        else:
            print("    (No content excerpt available or page loading failed)")
        
        print(f"\n{'-'*60}\n")

# === MAIN ===
if __name__ == "__main__":
    import json as pyjson
    print_banner()
    query = input("🔎 Enter your search query: ")
    fetch_proxies()

    try:
        results = duckduckgo_search(query, max_results=3)
        # Output results as JSON to a file
        with open("scrape_results.json", "w", encoding="utf-8") as f:
            pyjson.dump(results, f, ensure_ascii=False, indent=2)
        print("✅ Results saved to scrape_results.json")
    except Exception as main_e:
        print(pyjson.dumps({"error": str(main_e)}))