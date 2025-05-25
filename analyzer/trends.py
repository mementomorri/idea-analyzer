from pytrends.request import TrendReq


def get_trends_score(keyword: str) -> float:
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([keyword], timeframe='today 12-m')
        data = pytrends.interest_over_time()
        if data.empty:
            return 0.0
        return round(float(data[keyword].mean()), 2)
    except Exception:
        return 0.0
