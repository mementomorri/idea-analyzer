import requests
from bs4 import BeautifulSoup


def fetch_comments(keyword: str) -> list[str]:
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/search/?q={keyword}'
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return [h3.text for h3 in soup.find_all('h3')][:5]
