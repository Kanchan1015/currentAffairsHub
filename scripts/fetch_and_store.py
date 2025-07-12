from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.news import Base
from app.scraping.rss_scraper import fetch_articles_from_feed
from app.db.news_ops import insert_unique_articles
from app.scraping.feed_sources import RSS_FEEDS

DB_PATH = "sqlite:///data/news.db"
engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)
db = Session()

total_inserted = 0

for feed in RSS_FEEDS:
    print(f"\n🔍 Fetching from {feed['source']}...")

    articles = fetch_articles_from_feed(
        feed_url=feed["url"],
        source_name=feed["source"]
    )

    print(f"📦 Parsed {len(articles)} articles.")
    for article in articles:
        print(f"📰 {article.title[:70]}... → 📚 Category: {article.category}")

    count = insert_unique_articles(articles, db)
    print(f"✅ {count} new articles inserted.")
    total_inserted += count

print(f"\n🎉 Total new articles inserted: {total_inserted}")
