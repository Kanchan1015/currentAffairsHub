import streamlit as st
import subprocess

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.news import News
from datetime import datetime

# DB setup
engine = create_engine("sqlite:///data/news.db")
Session = sessionmaker(bind=engine)
session = Session()

st.title("🗞️ Current Affairs Hub")

# 🔁 Refresh Button
if st.button("🔁 Refresh News"):
    with st.spinner("Fetching latest articles..."):
        subprocess.run(["python3", "-m", "scripts.fetch_and_store"])
        st.success("News updated!")
        st.rerun()

# 🔽 Category Filter Dropdown
categories = session.query(News.category).distinct().all()
category_list = sorted([c[0] for c in categories if c[0]])  # remove None
selected_category = st.selectbox("📚 Filter by Category", ["All"] + category_list)

# 📰 Query articles based on selection
query = session.query(News)
if selected_category != "All":
    query = query.filter(News.category == selected_category)

articles = query.order_by(News.published_at.desc()).limit(50).all()

for article in articles:
    st.subheader(article.title)
    st.write(f"🕒 {article.published_at.strftime('%Y-%m-%d %H:%M')}")
    st.write(f"📰 Source: {article.source} | 📚 Category: {article.category}")
    st.write(article.summary)
    st.markdown(f"[Read More]({article.url})", unsafe_allow_html=True)
    st.markdown("---")
