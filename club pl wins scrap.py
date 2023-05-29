import requests
from bs4 import BeautifulSoup
import pandas as pd


def wins():
    # URL of the Premier League website
    url = f"https://www.premierleague.com/stats/top/clubs/wins?se=-1"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the club data

    loop = soup.find_all("tr")
    # Initialize empty lists to store club names and win counts
    clubs = []
    wins = []

    # Extract the club names and win counts from the table rows
    for row in loop:
        club_cell = row.find("a", class_="playerName")
        win_cell = row.find("td", class_="mainStat text-centre")

        if club_cell or win_cell:
            club = club_cell.text.strip()
            win_count = int(win_cell.get_text(strip=True))

            clubs.append(club)
            wins.append(win_count)

    # Create a DataFrame using the extracted data
    data = {
        "Club": clubs,
        "Wins": wins
    }
    df = pd.DataFrame(data)
    print(df)
    for i, j in zip(clubs,wins):
        if j > 500:
            print(f"{i} is a top club")
    print("As they have the most wins in Premier league history")
    # Display the DataFrame in table format


wins()
