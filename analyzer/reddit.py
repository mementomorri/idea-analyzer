import requests
from bs4 import BeautifulSoup


def fetch_comments(keyword: str) -> list[str]:
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/search/?q={keyword}'
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        return [h3.text for h3 in soup.find_all('h3')][:5]
    except Exception:
        return ["No comments found or failed to fetch."]
