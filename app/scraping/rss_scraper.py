# app/scraping/rss_scraper.py

import feedparser
from datetime import datetime
from app.models.news import News

def fetch_articles_from_feed(feed_url, category, source_name):
    """
    Parses an RSS feed and returns a list of News objects (not inserted yet).
    """
    parsed_feed = feedparser.parse(feed_url)

    articles = []
    for entry in parsed_feed.entries:
        title = entry.get("title")
        summary = entry.get("summary", "")
        url = entry.get("link")
        published = entry.get("published", None)
        thumbnail = ""

        # Handle optional thumbnail (if available)
        if "media_thumbnail" in entry:
            thumbnail = entry.media_thumbnail[0].get("url", "")

        # Convert published date to datetime
        try:
            published_at = datetime(*entry.published_parsed[:6]) if published else None
        except Exception:
            published_at = None

        article = News(
            title=title,
            summary=summary,
            url=url,
            source=source_name,
            category=category,
            published_at=published_at,
            scraped_at=datetime.now(),
            thumbnail_url=thumbnail
        )
        articles.append(article)

    return articles
