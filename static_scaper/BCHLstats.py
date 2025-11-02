import requests
from bs4 import BeautifulSoup

url = "https://bchl.ca/stats/player-stats?sort=points"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

players = []
for row in soup.select("table-container tbody tr"):
    cols = row.find_all("td")
    players.append({
        "name": cols[3].text.strip(),
        "birthdate_year": cols[7].text.strip(),
        "jersey_number": int(cols[4].text),
    })
