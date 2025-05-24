import os
import json
import click
from dotenv import load_dotenv
from analyzer.trends import get_trends_score

load_dotenv()

from analyzer.reddit import fetch_comments
from analyzer.openai_client import (
    analyze_sentiment,
    get_market_insights,
    generate_features,
    get_competitiveness_insight,
)
from analyzer.github_analysis import count_repositories


@click.command()
@click.option('--idea', '-i', required=True, help='Product idea description')
def analyze(idea):
    report = {}
    report['idea'] = idea
    report['trend_interest'] = get_trends_score(idea)

    comments = fetch_comments(idea)
    score, quotes = analyze_sentiment(comments)
    report['sentiment_score'] = score
    report['representative_quotes'] = quotes

    report['market_insights'] = get_market_insights(idea)
    report['recommended_features'] = generate_features(idea)

    count = count_repositories(idea)
    report['competitor_count'] = count
    report['competitiveness_insight'] = get_competitiveness_insight(idea, count)

    tech_stack = [
        'Frontend: React',
        'Backend: FastAPI',
        'Database: PostgreSQL',
        'AI: OpenAI GPT-4',
        'Deployment: Docker, AWS/GCP',
    ]
    timeline = {
        'Week 1': 'Validation & Specs',
        'Week 2': 'Prototype & Design',
        'Week 3': 'Backend & AI Integration',
        'Week 4': 'Beta & Feedback',
        'Week 5': 'Deploy & Monitor',
    }
    report['suggested_tech_stack'] = tech_stack
    report['implementation_timeline'] = timeline

    click.echo(json.dumps(report, indent=2))


if __name__ == '__main__':
    analyze()
