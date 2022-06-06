import csv
import NFLFantasyFootball
import config

import create_draft_results as dr

"""Creates a CSV of up-to-date or season-end rosters for each fantasy team in the league AND shows those players 
draft positions from that same season. """

LEAGUE_ID = config.LEAGUE_ID
SEASON_END_YEAR = config.SEASON_END_YEAR


def export_draft_rosters_to_csv(draft_results: dict):
    with open('rosters_with_draft.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Create Header
        writer.writerow(['PlayerId',
                         'PlayerName',
                         'DraftPosition',
                         'DraftRound',
                         'DraftingTeamName',
                         'DraftingTeamManager',
                         'DraftingTeamId',
                         'FantasyTeamId',
                         'FantasyTeamName'
                         ])
        # Write Data
        for k, v in draft_results.items():
            writer.writerow(
                [k,  # PlayerId
                 v.get('PlayerName', None),
                 v.get('DraftPosition', None),
                 v.get('DraftRound', None),
                 v.get('DraftingTeamName', None),
                 v.get('DraftingTeamManager', None),
                 v.get('DraftingTeamId', None),
                 v.get('FantasyTeamId', None),
                 v.get('FantasyTeamName', None)
                 ])


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
