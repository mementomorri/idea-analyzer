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

Returns a full JSON report with all analyses.

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

