import httpx
import urllib.parse
import os


async def count_repositories(keyword: str) -> int:
    encoded_query = urllib.parse.quote_plus(keyword.strip())
    url = f'https://api.github.com/search/repositories?q={encoded_query}'
    headers = {}

    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers['Authorization'] = f'token {token}'

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            return resp.json().get('total_count', 0)
    except Exception:
        return 0
