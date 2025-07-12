# scripts/init_db.py

from sqlalchemy import create_engine
from app.models.news import Base

engine = create_engine('sqlite:///data/news.db')
Base.metadata.create_all(engine)

print("Database initialized and tables created.")
