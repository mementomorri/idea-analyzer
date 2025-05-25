import json
import asyncio
import click
from dotenv import load_dotenv

load_dotenv()

from analyzer.trends import get_trends_score
from analyzer.reddit import fetch_comments
from analyzer.openai_client import (
    analyze_sentiment,
    get_market_insights,
    generate_features,
    get_competitiveness_insight,
    get_tech_stack,
    get_timeline,
)
from analyzer.github_analysis import count_repositories


@click.command()
@click.option('--idea', '-i', required=True, help='Product idea description')
@click.option('--debug', is_flag=True, help='Enable debug output')
def cli(idea, debug):
    asyncio.run(analyze(idea, debug))


async def analyze(idea: str, debug: bool):
    report = {"idea": idea}
    errors = {}

    try:
        results = await asyncio.wait_for(
            asyncio.gather(
                get_trends_score(idea),
                fetch_comments(idea),
                get_market_insights(idea),
                generate_features(idea),
                count_repositories(idea),
                get_tech_stack(idea),
                get_timeline(idea),
                return_exceptions=True,
            ),
            timeout=90,
        )

        trend_score, comments, insights, features, count, tech_stack, timeline = results

        # Trend Score
        report["trend_interest"] = (
            trend_score if isinstance(trend_score, float) else 0.0
        )
        if debug and trend_score == 0.0:
            errors["trend_interest"] = (
                "Returned 0. Possibly due to obscure keyword or pytrends block."
            )

        # Sentiment from Reddit
        if isinstance(comments, list):
            sentiment_score, quotes = await analyze_sentiment(comments)
            report["sentiment_score"] = sentiment_score
            report["representative_quotes"] = quotes
        else:
            report["sentiment_score"] = 0.0
            report["representative_quotes"] = ["Error fetching Reddit comments"]
            errors["sentiment"] = str(comments)

        # Market Insights
        report["market_insights"] = (
            insights
            if isinstance(insights, str)
            else "Market insight generation failed."
        )

        # Feature Ideas
        report["recommended_features"] = (
            features if isinstance(features, list) else ["Feature generation failed"]
        )

        # GitHub Repos
        repo_count = count if isinstance(count, int) else 0
        report["competitor_count"] = repo_count

        if isinstance(repo_count, int):
            report["competitiveness_insight"] = await get_competitiveness_insight(
                idea, repo_count
            )
        else:
            report["competitiveness_insight"] = "Failed to analyze GitHub data"

        # Tech Stack and Timeline
        report["suggested_tech_stack"] = (
            tech_stack
            if isinstance(tech_stack, list)
            else ["Tech stack generation failed"]
        )
        report["implementation_timeline"] = (
            timeline
            if isinstance(timeline, dict)
            else {"Timeline": "Failed to generate"}
        )

    except asyncio.TimeoutError:
        report["error"] = (
            "⚠️ Analysis timed out after 30 seconds. Try again with simpler input."
        )
    except Exception as e:
        report["error"] = f"Critical error during analysis: {e}"

    click.echo(json.dumps(report, indent=2))

    if debug and errors:
        click.echo("\n[DEBUG INFO]", err=True)
        for key, msg in errors.items():
            click.echo(f"- {key}: {msg}", err=True)


if __name__ == '__main__':
    cli()
