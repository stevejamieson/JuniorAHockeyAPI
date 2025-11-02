from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://nojhl.com/stats/player-stats")
    page.wait_for_selector("table")  # Wait for the table to load

    soup = BeautifulSoup(page.content(), "html.parser")
    skaters = []

    for row in soup.select("table tbody tr"):
        cols = row.find_all("td")
        if len(cols) >= 10:
            skaters.append({
                "name": cols[4].text.strip(),
                "position": cols[7].text.strip(),
                "team": cols[6].text.strip(),
                "GP": cols[8].text.strip(),
                "G": cols[9].text.strip(),
                "A": cols[10].text.strip(),
                "Points": cols[11].text.strip(),

            })

    browser.close()

print(skaters)
