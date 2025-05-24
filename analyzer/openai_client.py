import os
import re
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def analyze_sentiment(comments: list[str]) -> tuple[float, list[str]]:
    text = "\n".join(comments)
    resp = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'system',
                'content': 'Analyze sentiment (0-1) and give two representative quotes.',
            },
            {'role': 'user', 'content': text},
        ],
        max_tokens=100,
    )
    out = resp.choices[0].message.content.split('\n')
    score, quotes = 0.0, []
    for line in out:
        sentiment = line.find('Sentiment Score')
        if sentiment != -1:
            score_raw = line.split(':')[1].strip()
            score = float(re.findall(r'\d+\.\d+', score_raw)[0])
            quotes = eval(line.split(':', 1)[1].strip())
            break
    return score, quotes


def get_market_insights(keyword: str) -> str:
    prompt = f"Provide market insights and growth stats for '{keyword}'."
    resp = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': prompt}],
        max_tokens=100,
    )
    return resp.choices[0].message.content.strip()


def generate_features(keyword: str) -> list[str]:
    prompt = f"Suggest 3 MVP features for an app described as '{keyword}'."
    resp = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': prompt}],
        max_tokens=100,
    )
    return [
        line.lstrip('- ').strip()
        for line in resp.choices[0].message.content.split('\n')
        if line
    ]


def get_competitiveness_insight(keyword: str, count: int) -> str:
    prompt = f"There are {count} GitHub repos for '{keyword}'. Analyze niche competitiveness."
    resp = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': prompt}],
        max_tokens=100,
    )
    return resp.choices[0].message.content.strip()
