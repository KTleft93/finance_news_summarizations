from finlight_client import FinlightApi, ApiConfig
from finlight_client.models import GetArticlesParams, GetArticleByLinkParams
import os
from dotenv import load_dotenv

load_dotenv()

client = FinlightApi(config=ApiConfig(api_key=os.getenv("FINLIGHT_API")))

# yahoofinance only, change query for context
def get_finlight_news(query="SPY", pageSize=10):
    """
    Fetch news articles from API client.
    Returns a list of article objects.
    """
    try:
        params = GetArticlesParams(
            query=query,
            sources=["finance.yahoo.com"],
            pageSize=pageSize
        )
        articles = client.articles.fetch_articles(params=params)
        return articles.articles
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
