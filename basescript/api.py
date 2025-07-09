# === api working version using basescript (scraper_base.py)===

from fastapi import FastAPI
from scraper_base import duckduckgo_search, fetch_proxies
import uvicorn

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Preload proxies once at startup
    fetch_proxies()

@app.get("/scrape")
async def scrape(query: str):
  results = duckduckgo_search(query, max_results=3)
  return results

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)