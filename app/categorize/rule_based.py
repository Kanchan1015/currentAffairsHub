CATEGORY_KEYWORDS = {
    "Tech": ["AI", "Apple", "Google", "Microsoft", "cloud", "startup", "software", "chip", "data"],
    "Gaming": ["game", "Xbox", "PlayStation", "Nintendo", "Steam", "gamer", "Ubisoft", "Battlefield"],
    "Politics": ["election", "parliament", "senate", "congress", "modi", "biden", "policy", "campaign"],
    "Science": ["research", "study", "quantum", "climate", "experiment", "space", "nasa", "biology"],
    "Startups/AI": ["startup", "funding", "Series A", "machine learning", "VC", "AI", "neural", "GPT"]
}

def categorize_article(title, summary):
    combined_text = f"{title} {summary}".lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in combined_text:
                return category
    return "Uncategorized"
