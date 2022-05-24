import requests
from bs4 import BeautifulSoup


class LeagueConfig:
    """
    :param season_end_year: Set a year to retrieve the season-end roster for the year. You'll especially need to do
    this after a season ends, but before the new one starts.
    """

    def __init__(self,
                 league_id: int = None,
                 season_end_year: int = None):

        self.league_id = league_id
        if league_id is None:
            raise BaseException("league_id is a required argument")

        self.league_home_url = f"https://fantasy.nfl.com/league/{self.league_id}/"
        self.draft_results_url = f"https://fantasy.nfl.com/league/{self.league_id}/draftresults?draftResultsDetail=0&draftResultsTab=round&draftResultsType=results"
        self.taken_players_url = f"https://fantasy.nfl.com/league/{self.league_id}/players?playerStatus=owned"
        self.league_settings_url = f"https://fantasy.nfl.com/league/{self.league_id}/settings"

        if season_end_year:
            self.season_end_year = season_end_year
            self.draft_results_url = f"https://fantasy.nfl.com/league/{league_id}/history/{season_end_year}/draftresults?draftResultsDetail=0&draftResultsTab=round&draftResultsType=results"

    @staticmethod
    def get_request(url):
        error_message = """'Unable to connect to NFL Fantasy Football. Make sure the league is set to public or that 
        you're logged into NFL.com fantasy football.' """

        r = requests.get(url)
        if r.status_code != 200:
            raise ConnectionRefusedError(error_message)
        return r

    def get_league_settings(self):
        r = self.get_request(self.league_settings_url)
        s = BeautifulSoup(r.content, 'html.parser')
        return s

    def get_number_of_teams(self) -> range:
        league_settings_soup = self.get_league_settings()

        league_settings = league_settings_soup.find_all('div')

        # Get the number of Teams in the League from Settings
        for i in league_settings:
            if i.previous == 'Teams':
                number_of_teams = i.contents[0]

                team_id_numbers = range(1, int(number_of_teams) + 1)

                return team_id_numbers


class NFLFantasyFootballSoup(LeagueConfig):

    def get_draft_results(self):
        r = self.get_request(self.draft_results_url)
        s = BeautifulSoup(r.content, 'html.parser').find('div', class_='results')
        return s

    def get_all_taken_players(self):
        r = self.get_request(self.taken_players_url)
        s = BeautifulSoup(r.content, 'html.parser')
        return s

    def get_team_roster_by_team_id(self, team_id=None):

        """Creates team rosters by team id.
         :param team_id: team ID
         """

        team_roster_url = f"https://fantasy.nfl.com/league/{self.league_id}/team/{team_id}"
        if self.season_end_year:
            team_roster_url = f"https://fantasy.nfl.com/league/{self.league_id}/history/{self.season_end_year}/teamhome?teamId={team_id}"

        r = self.get_request(team_roster_url)
        s = BeautifulSoup(r.content, 'html.parser')
        return s

    def get_league_home(self):
        r = self.get_request(self.league_home_url)
        s = BeautifulSoup(r.content, 'html.parser')

        return s
