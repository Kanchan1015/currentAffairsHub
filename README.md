# 🗞️ Current Affairs Hub

**Current Affairs Hub** is a full-stack Python project designed to help you **learn web scraping, data processing, storage, categorization, and frontend visualization** using real-world current affairs from trusted news sources. It scrapes news articles via RSS feeds, categorizes them using rule-based logic, stores them in an SQLite database, and displays them in a clean dashboard using Streamlit.

> ⚡ This project was built with learning as the top priority — each phase is structured to gradually teach concepts and build hands-on skills.

---

## 🔍 Table of Contents

- [Features](#features)
- [How It Works (Explained)](#how-it-works-explained)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Tech Stack](#tech-stack)
- [License](#license)

---

## ✅ Features

- 🔍 Scrapes articles from RSS feeds (TechCrunch, IGN, ScienceDaily, BBC, etc.)
- 🧠 Classifies articles into categories like Tech, Science, Politics, Gaming, etc.
- 🧾 Stores data in a SQLite database with no duplicates
- 🖥️ Streamlit dashboard with filter tabs and refresh functionality
- 🧰 Easy to extend and modular design
- 🧪 Built step-by-step to improve learning and debugging

---

## 🧠 How It Works (Explained)

This section explains **what each module does** and **why we need it**:

### 1. `rss_scraper.py` — **Scraping News via RSS**

- Uses `feedparser` to fetch articles from RSS feed URLs.
- Each feed provides a list of articles (`title`, `summary`, `link`, `published`, etc.).
- Outputs a list of articles in a standard Python dict format.

📚 **Concepts Learned**: RSS parsing, feed structures, basic Python dictionaries.

---

### 2. `categorizer.py` — **Classifying Articles**

- Uses simple **keyword-based logic** to assign a category (e.g., "AI", "Politics", "Science") based on words found in the title and summary.
- If nothing matches, defaults to `"Uncategorized"`.

📚 **Concepts Learned**: Rule-based classification, working with strings and lists, improving logic.

---

### 3. `news.py` — **Creating the Database Model**

- Defines a `News` class using SQLAlchemy.
- Maps Python objects to rows in a SQLite table called `news`.

📚 **Concepts Learned**: Object Relational Mapping (ORM), working with databases in Python.

---

### 4. `news_ops.py` — **Inserting & Deduplication**

- Checks for duplicate `url` before inserting to avoid repeated articles.
- Handles inserting articles with timestamp and category.

📚 **Concepts Learned**: Deduplication, database sessions, and clean data handling.

---

### 5. `fetch_and_store.py` — **Orchestrator Script**

- Fetches feeds → categorizes → inserts into database.
- You can run it manually or trigger it via Streamlit refresh button.

📚 **Concepts Learned**: Integration logic, modular functions, automation.

---

### 6. `main.py` (Streamlit) — **Dashboard**

- Displays articles using `st.write()` and markdown links.
- Has category filters and a "Refresh" button to re-fetch live data.

📚 **Concepts Learned**: Frontend thinking, Streamlit components, dynamic filtering.

---

## 📁 Project Structure

```

currentAffairsHub/
├── app/
│   ├── categorizer/            # Keyword-based logic
│   ├── db/                     # Insert logic with deduplication
│   ├── models/                 # SQLAlchemy ORM for news
│   └── scraping/               # Feed sources and scraping logic
├── data/                       # news.db lives here
├── scripts/                    # CLI scripts for setup/fetch
├── streamlit\_app/              # Dashboard UI
├── .gitignore
├── requirements.txt
└── README.md

```

---

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/currentAffairsHub.git
cd currentAffairsHub
```

2. **Create a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

4. **Initialize the database**

```bash
python3 -m scripts.init_db
```

5. **Fetch and store articles**

```bash
python3 -m scripts.fetch_and_store
```

6. **Run the dashboard**

```bash
streamlit run streamlit_app/main.py
```

---

## 📦 Tech Stack

| Tool          | Purpose                        |
| ------------- | ------------------------------ |
| Python        | Core language                  |
| feedparser    | RSS feed parsing               |
| SQLAlchemy    | Database ORM                   |
| SQLite        | Lightweight storage            |
| Streamlit     | Frontend dashboard             |
| BeautifulSoup | (Reserved for future scraping) |

---

## 📅 Phased Learning Progress

| Phase | Description          | Status             |
| ----- | -------------------- | ------------------ |
| 1     | Planning & Setup     | ✅ Done            |
| 2     | RSS Feed Scraping    | ✅ Done            |
| 3     | Categorization Logic | ✅ Done            |
| 4     | Data Storage         | ✅ Done            |
| 5     | Streamlit Dashboard  | ✅ Done            |
| 6     | Dockerization        | ⏳ Skipped for now |

---

## 🙌 Credits

- Built by **Kanchan**, guided by ChatGPT
- Inspired by the need to learn _how real web applications are built_
