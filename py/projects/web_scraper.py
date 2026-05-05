# =============================================================================
# PROJECT: Python Web Scraper
# =============================================================================
# TODO 1 (Mini): Scrape Hacker News front page
#   pip install requests beautifulsoup4
#   - Fetch https://news.ycombinator.com/
#   - Parse: rank, title, URL, score, comment count
#   - Save to hn_<date>.json
#
# TODO 2 (Intermediate): Multi-page + rate limiting
#   - Scrape pages 1-5 (query param p=1..5)
#   - Respect robots.txt (urllib.robotparser)
#   - Delay between requests (time.sleep(1))
#   - Retry on 429/503 with exponential backoff
#   - Store in SQLite (avoid duplicates)
#
# TODO 3 (Advanced): Async with aiohttp
#   pip install aiohttp
#   - Concurrent fetching with asyncio.Semaphore(5)
#   - Cache already-scraped URLs in SQLite
#   - Export to CSV + JSON
#
# Run: python web_scraper.py
# =============================================================================

import json, time
from datetime import date

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Run: pip install requests beautifulsoup4")
    raise

HN_URL = "https://news.ycombinator.com/"

def scrape_page(page: int = 1) -> list[dict]:
    """TODO: fetch and parse one HN page, return list of story dicts"""
    url = f"{HN_URL}?p={page}"
    # resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    # soup = BeautifulSoup(resp.text, "html.parser")
    # ... parse .athing rows
    return []

def save_results(items: list[dict], filename: str = None) -> None:
    """TODO: save items list to JSON file"""
    if filename is None:
        filename = f"hn_{date.today()}.json"
    # with open(filename, "w") as f: json.dump(items, f, indent=2)

def main():
    all_items = []
    for page in range(1, 4):
        items = scrape_page(page)
        all_items.extend(items)
        time.sleep(1)
    save_results(all_items)
    print(f"Scraped {len(all_items)} stories")

if __name__ == "__main__":
    main()
