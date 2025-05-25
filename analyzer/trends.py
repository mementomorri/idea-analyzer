import re
from pytrends.request import TrendReq
import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="pytrends")


def simplify_keyword(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]+', ' ', text).strip().lower()


async def get_trends_score(keyword: str) -> float:
    try:
        simplified = simplify_keyword(keyword)
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([simplified], timeframe='today 12-m')
        data = pytrends.interest_over_time()
        if data.empty or simplified not in data.columns:
            return 0.0
        return round(data[simplified].mean(), 2)
    except Exception:
        return 0.0
