import requests
from bs4 import BeautifulSoup


def get_draft_results(league_id):
    url = f"https://fantasy.nfl.com/league/{league_id}/draftresults?draftResultsDetail=0&draftResultsTab=round&draftResultsType=results"

    # Get draft data from Request
    r = requests.get(url)

    # Raise exception if connection is not successful
    if r.status_code != 200:
        raise ConnectionRefusedError(f"""Unable to connect to NFL Fantasy Football. 
        Make sure the league is set to public or that you're logged into NFL.com fantasy football.
        HTTP Request Status code = {r.status_code}""")

    # Parsing the HTML to only draft results div
    s = BeautifulSoup(r.content, 'html.parser').find('div', class_='results')

    return s


def get_all_taken_players(league_id):
    url = f"https://fantasy.nfl.com/league/{league_id}/players?playerStatus=owned"

    r = requests.get(url)

    if r.status_code != 200:
        raise ConnectionRefusedError(f"""Unable to connect to NFL Fantasy Football. 
        Make sure the league is set to public or that you're logged into NFL.com fantasy football.
        HTTP Request Status code = {r.status_code}""")

    s = BeautifulSoup(r.content, 'html.parser')

    return s
