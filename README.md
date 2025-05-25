# 💡 Idea Analyzer

Analyze startup ideas using search trends, Reddit discussions, GitHub activity, and AI insights. This was made over a couple of hours on a weekend and doesn't tend to be something serious.

## 🚀 Features

- 📈 Google Trends score
- 💬 Reddit sentiment analysis
- 🧠 Market insights, MVP features (via OpenAI)
- 🛠 GitHub repo count & competitiveness
- 📋 Full JSON report with tech stack & timeline

## ⚙️ Setup

```bash
git clone https://github.com/mementomorri/idea-analyzer.git
cd idea-analyzer
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
```

Create a `.env`:

```env
OPENAI_API_KEY=your_key_here
# Optional: GITHUB_TOKEN=...
```

## 🧪 Usage

```bash
python analyzer.cli.py --idea "AI-powered tutor for kids"
```

Returns a full JSON report with all analyses. Example output:

```
$ python -m analyzer.cli -i="bitcoin predictor"
{
  "idea": "=bitcoin predictor",
  "trend_interest": 6.11,
  "sentiment_score": 0.7,
  "representative_quotes": [
    "Investing in cryptocurrency can be volatile, but educating yourself is key to making informed decisions.",
    "The community around cryptocurrencies often shares valuable insights and predictions for the market."
  ],
  "market_insights": "As of my last update in October 2023, I don't have specific insights or growth statistics for a product or service specifically named \"=bitcoin p
redictor.\" However, I can provide general insights regarding the Bitcoin prediction and analytics market.\n\n### Market Insights for Bitcoin Predictors and Analytics:\
n\n1. **Background**: The cryptocurrency market, particularly Bitcoin, has gained massive traction and legitimacy over the past several years. Traders and investors inc
reasingly rely on predictive analytics to make informed decisions.\n\n2. **Market Growth**:",
  "recommended_features": [
    "Creating a minimum viable product (MVP) for a Bitcoin predictor app involves identifying essential features that deliver value to users while allowing for rapid de
velopment and testing. Here are three core features you might consider:",
    "1. **Price Prediction Algorithm**:",
    "Integrate a basic yet effective algorithm that analyzes historical price data, market trends, and other relevant factors (e.g., trading volume, social media sentim
ent, etc.) to provide short-term price predictions for Bitcoin. This feature can include visualizations like graphs"
  ],
  "competitor_count": 1529,
  "competitiveness_insight": "Analyzing the competitiveness of repositories for the keyword \"=bitcoin predictor\" on GitHub involves considering several factors such a
s the number of repositories, the quality and activity of those repositories, user engagement, and broader market trends in the cryptocurrency and prediction markets.\n
\n### 1. Quantity of Repositories\n- **1529 Repositories**: A high number of repositories indicates significant interest or potential demand for Bitcoin prediction tool
s. This suggests a crowded niche, which means standing out may be challenging.\n\n### 2.",
  "suggested_tech_stack": [
    "To develop an app like a Bitcoin predictor, you'll need a stack that supports data collection, analysis, and user interaction. Here\u2019s a list of suitable techn
ologies across different layers of the application:",
    "### Frontend",
    "1. **React.js** - A popular JavaScript library for building user interfaces, perfect for single-page applications.",
    "2. **Vue.js** - An alternative to React that is also great for building interactive UIs with a simpler learning curve.",
    "3. **Angular** - A robust framework for creating dynamic web applications with a rich set of features.",
    "4. **D3.js** - For data visualization, particularly useful for visualizing historical Bitcoin price trends and prediction results.",
    "5. **Tailwind CSS / Bootstrap** - CSS frameworks for"
  ],
  "implementation_timeline": {
    "### Week 1": "Research & Requirement Analysis",
    "### Week 2": "Data Collection & Setup",
    "### Week 3": "Model Development"
  }
}
```

## 🧠 Local LLM Option

Swap OpenAI API with local models (e.g. via `llama-cpp-python`, `transformers`, or `ollama`).

## 📦 Tech

- `click`, `requests`, `beautifulsoup4`
- `openai` or alternative
- `pytrends`, GitHub API
- Optional: local LLMs

## ⚠️ Notes

- Reddit scraping may break (no API).
- OpenAI usage may incur costs — local fallback suggested.
- GitHub rate-limits: set GITHUB_TOKEN in .env for higher quota

## 📄 License

MIT – use freely, credit appreciated.
