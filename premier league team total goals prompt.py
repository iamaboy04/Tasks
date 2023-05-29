import requests
from bs4 import BeautifulSoup

def display_goals_scored(club_id):
    # URL of the Premier League website
    url = f"https://www.premierleague.com/clubs/{club_id}/club/stats"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    team_element = soup.find("h1", class_="team js-team")

    if team_element:
        team_name = team_element.text.strip()
        print(f"{team_name}")
    # Find the element containing the goals scored
    goals_element = soup.find("span", class_="allStatContainer statgoals")

    if goals_element:
        # Extract the goals scored value
        goals_scored = goals_element.text.strip()
        print(f"Goals scored in Premier league: {goals_scored}")
    else:
        print(f"Unable to find goals scored for Club ID {club_id}.")


# Example usage
club_id = input("Enter club id: ")
display_goals_scored(club_id)
