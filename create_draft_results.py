import csv
from util import get_soup as gs
import config

LEAGUE_ID = config.LEAGUE_ID


def create_draft_results_dict(league_id: int):
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

    return draft_dict


def export_team_rosters_to_csv(draft_results: dict):
    with open('nfl_fantasy_draft_order.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Create Header
        writer.writerow(['player_id',
                         'PlayerName',
                         'DraftPosition',
                         'DraftRound',
                         'DraftTeamID',
                         'FantasyTeam'])
        # Write Data
        for k, v in draft_results.items():
            writer.writerow(
                [k,
                 v['PlayerName'],
                 v['DraftPosition'],
                 v['DraftRound'],
                 v['DraftTeamID'],
                 v['FantasyTeam']])


def main():
    draft_results_dict = create_draft_results_dict(LEAGUE_ID)
    export_team_rosters_to_csv(draft_results_dict)
