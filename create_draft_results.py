import csv
import NFLSoup
import config

"""Creates a CSV of fantasy draft results from current draft or specified year."""

LEAGUE_ID = config.LEAGUE_ID
SEASON_END_YEAR = config.SEASON_END_YEAR

nfls = NFLSoup.NFLFantasyFootballSoup(league_id=LEAGUE_ID, season_end_year=SEASON_END_YEAR)


def create_draft_results() -> dict:
    soup = nfls.get_draft_results()

    players = soup.findAll('a', class_='playerNameFull')

    draft_results = {}
    for i in players:
        player_id = int(i.attrs['href'].split('playerId=')[1])
        player_name = i.contents[0]
        draft_position = i.parent.parent.contents[0].contents[0].split('.')[0]
        draft_round = i.parent.parent.contents[0].parent.parent.parent.contents[0].contents[0].split(' ')[1]
        fantasy_team = i.parent.parent.contents[6].contents[0].text
        fantasy_manager = i.parent.parent.contents[6].contents[1].text
        fantasy_team_id = i.parent.parent.contents[5].attrs['class'][1].split('-')[1]
        draft_results.update({player_id: {"PlayerName": player_name,
                                          "DraftPosition": draft_position,
                                          "DraftRound": draft_round,
                                          "DraftingTeamName": fantasy_team,
                                          "DraftingTeamManager": fantasy_manager,
                                          "DraftingTeamId": fantasy_team_id}})

    return draft_results


def export_draft_results_to_csv(draft_results: dict):
    with open('nfl_fantasy_draft_order.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Create Header
        writer.writerow(['PlayerId',
                         'PlayerName',
                         'DraftPosition',
                         'DraftRound',
                         'DraftingTeamName',
                         'DraftingTeamManager',
                         'DraftingTeamId'])
        # Write Data
        for k, v in draft_results.items():
            writer.writerow(
                [k,  # PlayerId
                 v['PlayerName'],
                 v['DraftPosition'],
                 v['DraftRound'],
                 v['DraftingTeamName'],
                 v['DraftingTeamManager'],
                 v['DraftingTeamId']])


def main():
    draft_results_dict = create_draft_results()
    export_draft_results_to_csv(draft_results_dict)


main()
