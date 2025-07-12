# scripts/test_categorizer.py

from app.categorize.rule_based import categorize_article

sample_articles = [
    ("Apple launches new AI chip for MacBooks", "The chip is built for LLMs and edge inference."),
    ("Steam Summer Sale hits record downloads", "Gamers rush to grab PlayStation titles at discount."),
    ("NASA discovers water on Mars", "Breakthrough in planetary science."),
    ("Biden signs new policy into law", "Focus on tech and data security."),
    ("Series A funding for Chennai-based SaaS startup", "Led by Sequoia Capital.")
]

for title, summary in sample_articles:
    category = categorize_article(title, summary)
    print(f"\n📰 Title: {title}\n📚 Category: {category}")
