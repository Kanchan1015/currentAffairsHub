from sqlalchemy.orm import Session
from app.models.news import News

def insert_unique_articles(articles: list, db: Session):
    inserted_count = 0
    for article in articles:
        exists = db.query(News).filter_by(url=article.url).first()
        if not exists:
            db.add(article)
            inserted_count += 1
    db.commit()
    return inserted_count
