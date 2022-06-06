import csv
import NFLFantasyFootball
import config

"""Creates a CSV of up-to-date or season-end rosters for each fantasy team in the league."""

LEAGUE_ID = config.LEAGUE_ID
SEASON_END_YEAR = config.SEASON_END_YEAR


def export_team_rosters_to_csv(team_rosters: dict):
    with open('team_rosters.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Create Header
        writer.writerow(['player_id',
                         'PlayerName',
                         'PlayerPositionTeam',
                         'FantasyTeamId',
                         'FantasyTeamName'])
        # Write Data
        for k, v in team_rosters.items():
            writer.writerow(
                [k,
                 v['PlayerName'],
                 v['PlayerPositionTeam'],
                 v['FantasyTeamId'],
                 v['FantasyTeamName']])


def main():
    rosters = NFLFantasyFootball.LeagueTeams(league_id=LEAGUE_ID,
                                             season_end_year=SEASON_END_YEAR).create_team_rosters()
    export_team_rosters_to_csv(rosters)


main()
