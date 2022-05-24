from NFLSoup import NFLFantasyFootballSoup


class NFLFantasyFootballTeams(NFLFantasyFootballSoup):

    def get_fantasy_team_names(self) -> dict:
        league_home_soup = self.get_league_home()

        league_home_team_names = league_home_soup.find_all('a', class_='teamName')

        fantasy_team_names = {}

        for i in league_home_team_names:
            fantasy_team_names[int(i.attrs['href'].split('/')[-1:][0])] = i.contents[0]

        return fantasy_team_names

    def create_team_rosters(self) -> dict:
        number_of_teams = self.get_number_of_teams()
        fantasy_team_rosters = {}

        for team_id_number in number_of_teams:
            team_page = self.get_team_roster_by_team_id(team_id=team_id_number)
            team_page_players = team_page.find_all('a', class_='playerCard')

            for i in team_page_players:
                player_id = int(i.attrs['href'].split('playerId=')[1])
                if str(i.contents[0]) != 'View News':
                    player_name = str(i.contents[0])
                    fantasy_team_rosters.update({player_id: {"PlayerName": player_name,
                                                             "FantasyTeamId": team_id_number}})

        return fantasy_team_rosters
