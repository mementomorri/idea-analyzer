import os
import json
from openai import AsyncOpenAI

api_key = os.getenv('OPENAI_API_KEY')
client = AsyncOpenAI(api_key=api_key)


async def analyze_sentiment(comments: list[str]) -> tuple[float, list[str]]:
    text = "\n".join(comments)
    try:
        resp = await client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {
                    'role': 'system',
                    'content': 'Return JSON: {"score": float, "quotes": [str, str]}',
                },
                {'role': 'user', 'content': text},
            ],
            max_tokens=150,
        )
        content = resp.choices[0].message.content.strip()
        data = json.loads(content)
        if not isinstance(data, dict) or "score" not in data or "quotes" not in data:
            raise ValueError("Malformed sentiment response")
        return float(data["score"]), data["quotes"]
    except Exception as e:
        return 0.0, [f"Sentiment analysis failed: {e}"]


async def get_market_insights(keyword: str) -> str:
    prompt = f"Provide market insights and growth stats for '{keyword}'."
    try:
        resp = await client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=100,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Failed to fetch market insights: {e}"


async def generate_features(keyword: str) -> list[str]:
    prompt = f"Suggest 3 MVP features for an app described as '{keyword}'."
    try:
        resp = await client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=100,
        )
        return [
            line.lstrip('-•* ').strip()
            for line in resp.choices[0].message.content.split('\n')
            if line.strip()
        ]
    except Exception as e:
        return [f"Feature generation failed: {e}"]


async def get_competitiveness_insight(keyword: str, count: int) -> str:
    prompt = f"There are {count} GitHub repos for '{keyword}'. Analyze niche competitiveness."
    try:
        resp = await client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=100,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Failed to generate competitiveness insight: {e}"


async def get_tech_stack(idea: str) -> list[str]:
    prompt = f"What technologies (frontend, backend, database, AI, deployment) would suit an app idea like: '{idea}'? Return a list."
    try:
        resp = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
        )
        return [
            line.lstrip('-•* ').strip()
            for line in resp.choices[0].message.content.strip().split('\n')
            if line.strip()
        ]
    except Exception as e:
        return [f"Tech stack generation failed: {e}"]


async def get_timeline(idea: str) -> dict:
    prompt = f"Provide a 5-week development timeline for an MVP of: '{idea}'. Format as: Week N: Task."
    try:
        resp = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
        )
        lines = resp.choices[0].message.content.strip().split('\n')
        return {
            line.split(':', 1)[0].strip(): line.split(':', 1)[1].strip()
            for line in lines
            if ':' in line
        }
    except Exception as e:
        return {"Timeline generation failed": str(e)}
