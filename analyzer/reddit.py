import httpx
from bs4 import BeautifulSoup


async def fetch_comments(keyword: str) -> list[str]:
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/search/?q={keyword}'
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, 'html.parser')
            comments = [
                h3.text.strip() for h3 in soup.find_all('h3') if h3.text.strip()
            ]
            return (
                comments[:5] if comments else ["No relevant Reddit discussions found."]
            )
    except Exception as e:
        return [f"Failed to fetch Reddit comments: {e}"]
