import csv
import NFLFantasyFootball
import config

"""Creates a CSV of up-to-date or season-end rosters for each fantasy team in the league."""

LEAGUE_ID = config.LEAGUE_ID
SEASON_END_YEAR = config.SEASON_END_YEAR


def export_team_rosters_to_csv(team_rosters: dict):
    fieldnames = ['player_id',
                  'PlayerName',
                  'PlayerPositionTeam',
                  'FantasyTeamId',
                  'FantasyTeamName']

    with open('team_rosters.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for player_id, data in team_rosters.items():
            row = {'player_id': player_id}
            row.update(data)
            writer.writerow(row)


def main():
    rosters = NFLFantasyFootball.LeagueTeams(league_id=LEAGUE_ID,
                                             season_end_year=SEASON_END_YEAR).create_team_rosters()
    export_team_rosters_to_csv(rosters)


main()
