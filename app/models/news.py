from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    summary = Column(Text)
    url = Column(String, unique=True, nullable=False)
    source = Column(String)
    category = Column(String)
    published_at = Column(DateTime)
    scraped_at = Column(DateTime)
    thumbnail_url = Column(String)
