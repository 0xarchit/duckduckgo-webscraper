from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import webscraper

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def startup_event():
    # Fetch proxies once at startup
    webscraper.fetch_proxies()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # Build proxy options with counts
    proxy_options = []
    # Default built-in list
    webscraper.fetch_proxies(None)
    default_count = len(webscraper.proxy_list)
    proxy_options.append({
        "label": "Default (built-in)",
        "url": "",
        "count": default_count
    })
    # Preset proxy sources
    preset_sources = [
        ("mmpx12 proxy-list", "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/https.txt"),
        ("Proxy-List-World", "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt"),
        ("ErcinDedeoglu proxies", "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/refs/heads/main/proxies/https.txt"),
        ("Zaeem20 FREE_PROXIES_LIST", "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt"),
        ("SoliSpirit proxy-list", "https://raw.githubusercontent.com/SoliSpirit/proxy-list/refs/heads/main/https.txt"),
        ("databay-labs free-proxy-list", "https://raw.githubusercontent.com/databay-labs/free-proxy-list/refs/heads/master/https.txt")
    ]
    for lbl, url in preset_sources:
        webscraper.fetch_proxies(url)
        proxy_options.append({"label": lbl, "url": url, "count": len(webscraper.proxy_list)})
    # Render search form
    return templates.TemplateResponse("index.html", {"request": request, "proxy_options": proxy_options})

# Search endpoint with proxy source selection
@app.post("/search", response_class=HTMLResponse)
def search(request: Request,
           query: str = Form(...),
           proxy_source: str = Form(""),
           custom_proxy_url: str = Form("")):
    """
    Handle search form submission with optional proxy source selection.
    """
    # Determine effective proxy URL
    if proxy_source == 'custom' and custom_proxy_url:
        effective_proxy_url = custom_proxy_url
    elif proxy_source:
        effective_proxy_url = proxy_source
    else:
        effective_proxy_url = None

    # Fetch proxies based on selection
    webscraper.fetch_proxies(effective_proxy_url)
    error = None
    results = []
    try:
        results = webscraper.duckduckgo_search(query, max_results=3)
    except Exception as e:
        error = str(e)
    # Render results page
    return templates.TemplateResponse("results.html", {
        "request": request,
        "results": results,
        "query": query,
        "error": error,
        "proxy_url": effective_proxy_url
    })

# To run: uvicorn app:app --reload --host 0.0.0.0 --port 8000
