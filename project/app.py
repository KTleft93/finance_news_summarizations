from fetch_news import get_finlight_news
from page_crawl import page_crawler


data = get_finlight_news("SPY", 1)
yahoo_articles = [a for a in data if "finance.yahoo.com" in a.link]

for item in yahoo_articles:
    page_crawler(item.link)


"""
get link
crawl page 

"""

