# 📰 Current Affairs Hub

A lightweight Python + Streamlit web app that scrapes, categorizes, and displays current news across various domains like Tech, Gaming, Politics, Science, and Startups/AI — using free RSS feeds and no paid APIs.

---

## ✅ Project Goals

- Scrape reliable RSS feeds from tech, science, gaming, and news sites
- Store and deduplicate news in a structured SQLite database
- Categorize news using keyword rules or NLP
- Display a clean, searchable dashboard using Streamlit
- Learn backend architecture, Docker, Python, and clean code practices

---

## 📁 Project Structure

```

currentAffairsHub/
├── app/                  # Core Python logic (models, scraping, utils)
│   ├── models/           # SQLAlchemy News model
│   └── scraping/         # (Coming in Phase 2) RSS scraper
│
├── data/                 # SQLite database file
│   └── news.db
│
├── scripts/              # DB setup and test scripts
│   ├── init\_db.py
│   ├── demo\_insert.py
│   └── demo\_fetch.py
│
├── streamlit\_app/        # Frontend (TBD in Phase 3)
│   └── main.py
│
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md

```

---

## 🛠️ Phase 1: Setup Complete

- ✅ Git repository initialized with `.gitignore` and clean folder structure
- ✅ Python virtual environment created using `venv`
- ✅ SQLAlchemy installed and configured
- ✅ `News` table model defined
- ✅ SQLite database initialized with `news.db`
- ✅ Dummy articles inserted and queried for testing
- ✅ Project dependencies tracked via `requirements.txt`

---

## 🧠 Learning Highlights

- Used SQLAlchemy ORM to manage structured data without raw SQL
- Created modular project structure for clarity and scalability
- Debugged real-world Python env issues (PEP 668, venv, pip)
- Practiced clean commit habits and phase-based branching

---

## 🌱 Next Phase: RSS Scraping (In Progress)

- Set up feedparser to read from live RSS URLs
- Map RSS entries to News DB model
- Insert only new articles (deduplication by `url`)
- Store category, source, and thumbnail for frontend display

---

```

---

### ✅ How to Use It Going Forward

Every time we:

* Add a new component (e.g., RSS logic, Streamlit filters)
* Finish a phase

```
