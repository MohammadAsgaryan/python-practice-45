# 🌍 Country Scraper & Area Estimator  
A Python project that extracts country information from **ScrapeThisSite**, stores the data in a **SQLite database**, and estimates each country’s area based on its population.

---

## 📌 Features
- Scrapes country name and population from:  
  https://scrapethissite.com/pages/simple/
- Cleans and processes numeric data
- Stores results in a SQLite database (`countries.db`)
- Estimates land area using a simple population-based model
- Outputs sample results in the console

---

## 🛠 Technologies Used
- **Python 3**
- `requests`
- `beautifulsoup4`
- `sqlite3`

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone <repo-url>
cd <project-folder>
2. Install required packages

pip install requests beautifulsoup4

▶️ How to Run
Simply execute the Python script:
python practice.py

After running, a database file named countries.db will be generated in the project directory.
