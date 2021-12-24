import config
import csv
from util import get_soup as gs

league_id = config.LEAGUE_ID

soup = gs.get_draft_results(league_id)

players = soup.findAll('a', class_='playerNameFull')

draft_dict = {}
for i in players:
    player_id = int(i.attrs['href'].split('playerId=')[1])
    player_name = i.contents[0]
    draft_position = i.parent.parent.contents[0].contents[0].split('.')[0]
    draft_round = i.parent.parent.contents[0].parent.parent.parent.contents[0].contents[0].split(' ')[1]
    fantasy_team = i.parent.parent.contents[6].text
    fantasy_team_id = i.parent.parent.contents[5].attrs['class'][1].split('-')[1]
    draft_dict.update({player_id: {"PlayerName": player_name,
                                   "DraftPosition": draft_position,
                                   "DraftRound": draft_round,
                                   "FantasyTeam": fantasy_team,
                                   "FantasyTeamID": fantasy_team_id}})

with open('nfl_fantasy_draft_order.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['player_id', 'PlayerName', 'DraftPosition', 'DraftRound', 'FantasyTeamID', 'FantasyTeam'])
    for k, v in draft_dict.items():
        writer.writerow([k, v['PlayerName'], v['DraftPosition'], v['DraftRound'], v['FantasyTeamID'], v['FantasyTeam']])
