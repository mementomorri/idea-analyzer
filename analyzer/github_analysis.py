import requests


def count_repositories(keyword: str) -> int:
    url = f'https://api.github.com/search/repositories?q={keyword}'
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json().get('total_count', 0)
    except requests.RequestException:
        return 0
