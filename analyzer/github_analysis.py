import requests


def count_repositories(keyword: str) -> int:
    url = f'https://api.github.com/search/repositories?q={keyword}'
    resp = requests.get(url)
    return resp.json().get('total_count', 0)
