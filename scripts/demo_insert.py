from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.news import News

# 1. Connect to SQLite
engine = create_engine('sqlite:///data/news.db')
session = Session(bind=engine)

# 2. Create dummy articles
dummy_articles = [
    News(
        title="OpenAI launches new AI model",
        summary="OpenAI has released a new model capable of generating realistic text.",
        url="https://example.com/openai-launch",
        source="TechCrunch",
        category="Tech",
        published_at=datetime(2025, 7, 10, 10, 0),
        scraped_at=datetime.now(),
        thumbnail_url="https://example.com/thumb1.jpg"
    ),
    News(
        title="NASA announces Mars mission timeline",
        summary="NASA confirms mission to Mars is scheduled for 2030.",
        url="https://example.com/nasa-mars",
        source="ScienceDaily",
        category="Science",
        published_at=datetime(2025, 7, 9, 15, 30),
        scraped_at=datetime.now(),
        thumbnail_url="https://example.com/thumb2.jpg"
    ),
]

# 3. Insert into DB (skip duplicates)
for article in dummy_articles:
    if not session.query(News).filter_by(url=article.url).first():
        session.add(article)

# 4. Commit and close
session.commit()
session.close()

print("Dummy news inserted.")
