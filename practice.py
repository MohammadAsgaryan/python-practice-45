import requests
from bs4 import BeautifulSoup
import sqlite3

# ------------------------------
#  Create SQLite database
# ------------------------------

conn = sqlite3.connect("countries.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    population INTEGER,
    estimated_area REAL
);
""")
conn.commit()


# ------------------------------
#  Scrape function
# ------------------------------

def scrape_countries():
    url = "https://scrapethissite.com/pages/simple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    countries_html = soup.find_all("div", class_="country")

    results = []

    for c in countries_html:
        name = c.find("h3", class_="country-name").text.strip()
        population = c.find("span", class_="country-population").text.strip()

        # Convert to integer safely
        try:
            population = int(population.replace(",", ""))
        except:
            population = 0

        results.append((name, population))

    return results


# ------------------------------
#  Estimation function
# ------------------------------

def estimate_area(population):
    k = 0.00003
    return population * k


# ------------------------------
#  Main function
# ------------------------------

def main():
    countries = scrape_countries()

    for name, population in countries:
        estimated_area = estimate_area(population)

        cursor.execute("""
            INSERT INTO countries (name, population, estimated_area)
            VALUES (?, ?, ?)
        """, (name, population, estimated_area))

    conn.commit()

    print("Data stored successfully.\n")
    print("Sample output:")

    for row in cursor.execute("SELECT name, population, estimated_area FROM countries LIMIT 10;"):
        print(row)

    conn.close()


main()
