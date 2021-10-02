import config
import csv
import requests
from bs4 import BeautifulSoup

league_id = config.LEAGUE_ID

if not league_id:
    raise NameError('Must provide a league ID to generate draft order.')

url = f"https://fantasy.nfl.com/league/{league_id}/draftresults?draftResultsDetail=0&draftResultsTab=round&draftResultsType=results"

# Get draft data from Request
r = requests.get(url)

# Raise exception if connection is not successful
if r.status_code != 200:
    raise ConnectionRefusedError(f"""Unable to connect to Fantasy Football Draft Page. 
    Make sure the league is set to public or that you're logged into NFL.com fantasy football.
    HTTP Request Status code = {r.status_code}""")

# Parsing the HTML to only draft results div
s = BeautifulSoup(r.content, 'html.parser').find('div', class_='results')

players = s.findAll('a', class_='playerNameFull')

draft_dict = {}
for i in players:
    player_name = i.contents[0]
    draft_position = i.parent.parent.contents[0].contents[0].split('.')[0]
    draft_round = i.parent.parent.contents[0].parent.parent.parent.contents[0].contents[0].split(' ')[1]
    fantasy_team = i.parent.parent.contents[6].text
    draft_dict.update({player_name: {"DraftPosition": draft_position,
                                     "DraftRound": draft_round,
                                     "FantasyTeam": fantasy_team}})

with open('nfl_fantasy_draft_order.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['PlayerName', 'DraftPosition', 'DraftRound', 'FantasyTeam'])  # Create Header
    for k, v in draft_dict.items():
        writer.writerow([k, v['DraftPosition'], v['DraftRound'], v['FantasyTeam']])
