# app/scraping/rss_scraper.py

import feedparser
from app.models.news import News
from datetime import datetime
from app.categorize.rule_based import categorize_article  # ⬅️ Add this import

def fetch_articles_from_feed(feed_url, category=None, source_name=None):
    parsed_feed = feedparser.parse(feed_url)
    articles = []

    for entry in parsed_feed.entries:
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        published = entry.get("published", "")
        url = entry.get("link", "")

        # Convert published string to datetime (fallback if empty)
        try:
            published_date = datetime(*entry.published_parsed[:6])
        except Exception:
            published_date = datetime.now()

        # Use rule-based categorization if not passed
        final_category = category or categorize_article(title, summary)

        article = News(
            title=title,
            summary=summary,
            url=url,
            published_at=published_date,
            source=source_name or "Unknown",
            category=final_category
        )

        articles.append(article)

    return articles
