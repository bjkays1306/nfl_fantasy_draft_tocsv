import csv
import NFLFantasyFootball
import config

import create_draft_results as dr

"""Creates a CSV of up-to-date or season-end rosters for each fantasy team in the league AND shows those players 
draft positions from that same season. 

PlayerPosition field is the position the player played when drafted.
PlayerPositionTeam field is the position the player plays and the NFL team abbreviation, in one column.

"""

LEAGUE_ID = config.LEAGUE_ID
SEASON_END_YEAR = config.SEASON_END_YEAR


def export_draft_rosters_to_csv(draft_results: dict):
    fieldnames = ['PlayerId', 'PlayerName', 'PlayerPosition', 'PlayerPositionTeam', 'DraftPosition',
                  'DraftRound', 'DraftingTeamName', 'DraftingTeamManager', 'DraftingTeamId',
                  'FantasyTeamId', 'FantasyTeamName']

    with open('rosters_with_draft.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()  # Write the header

        for player_id, data in draft_results.items():
            row = {'PlayerId': player_id}
            row.update({field: data.get(field, None) for field in fieldnames[1:]})
            writer.writerow(row)


def main():
    rosters = NFLFantasyFootball.LeagueTeams(league_id=LEAGUE_ID,
                                             season_end_year=SEASON_END_YEAR).create_team_rosters()

    draft_results = dr.create_draft_results()

    dict3 = draft_results.copy()

    for key, value in rosters.items():
        if dict3.get(key, None):
            dict3[key].update(value)
        else:
            dict3[key] = value

    export_draft_rosters_to_csv(dict3)


main()
