from app.scraping.rss_scraper import fetch_articles_from_feed

# Example TechCrunch feed
url = "https://techcrunch.com/feed/"
category = "Tech"
source = "TechCrunch"

articles = fetch_articles_from_feed(url, category, source)

print(f"✅ Fetched {len(articles)} articles from {source}:\n")
for i, article in enumerate(articles[:5], 1):
    print(f"{i}. {article.title} ({article.published_at})")
