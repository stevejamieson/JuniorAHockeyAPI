from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://bchl.ca/stats/player-stats?sort=points")
    page.wait_for_selector("table")  # Wait for the table to load

    soup = BeautifulSoup(page.content(), "html.parser")
    skaters = []

    for row in soup.select("table tbody tr"):
        cols = row.find_all("td")
        if len(cols) >= 10:
            skaters.append({
                "name": cols[2].text.strip(),
                "jersey": cols[3].text.strip(),
                "position": cols[5].text.strip(),
                "birthdate": cols[6].text.strip(),
                "team": cols[7].text.strip(),
                "games_played": int(cols[8].text.strip()),
                "goals": int(cols[9].text.strip()),
                "assists": int(cols[10].text.strip()),
                "points": int(cols[11].text.strip()),
            })

    browser.close()

print(skaters)
