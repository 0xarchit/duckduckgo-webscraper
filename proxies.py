# credit: https://github.com/theriturajps/proxy-list

import requests
import re
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

SOURCES = [
    "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=https",
    # "https://proxylist.geonode.com/api/proxy-list?protocols=http,https&limit=500",
    # "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    # "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt"
]

def fetch_proxies(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            proxies = set()
            for line in response.text.split('\n'):
                line = line.strip()
                if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+$', line):
                    proxies.add(line)
            return proxies
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
    return set()

# Proxy testing function similar to scraper_base.py
def test_proxy(proxy):
    proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        response = requests.get("https://httpbin.org/ip", proxies=proxy_dict, timeout=5)
        if response.status_code == 200:
            print(f"✅ Proxy working: {proxy}")
            return True
    except requests.exceptions.RequestException:
        pass
    return False

def get_proxies():
    proxies = set()
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_proxies, url) for url in SOURCES]
        for future in as_completed(futures):
            try:
                proxies.update(future.result())
            except Exception as e:
                print(f"Error processing future: {str(e)}")

    print(f"Testing {len(proxies)} proxies for working status...")
    working_proxies = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_proxy = {executor.submit(test_proxy, proxy): proxy for proxy in proxies}
        for future in as_completed(future_to_proxy):
            proxy = future_to_proxy[future]
            try:
                if future.result():
                    working_proxies.append(proxy)
            except Exception:
                pass
    print(f"Found {len(working_proxies)} working proxies.")
    return sorted(working_proxies)

def save_proxies(proxies):
    # Save as TXT
    with open("proxies.txt", "w") as f:
        f.write("\n".join(proxies))
    
    # Save as JSON with metadata
    proxy_data = {
        "metadata": {
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "count": len(proxies),
            "sources": SOURCES
        },
        "proxies": proxies
    }
    with open("proxies.json", "w") as f:
        json.dump(proxy_data, f, indent=2)



if __name__ == "__main__":
    start_time = time.time()
    print("Starting proxy update...")
    proxies = get_proxies()  # Only working proxies returned
    save_proxies(proxies)
    elapsed = time.time() - start_time
    print(f"Updated {len(proxies)} working proxies in {elapsed:.2f} seconds")