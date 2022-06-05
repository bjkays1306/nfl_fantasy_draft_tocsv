from NFLFantasyFootball import LeagueSoup


class LeagueTeams(LeagueSoup):

    def get_fantasy_team_names(self) -> dict:
        league_home_soup = self.get_league_home()

        league_home_team_names = league_home_soup.find_all('a', class_='teamName')

        fantasy_team_names = {}

        if self.season_end_year:
            for i in league_home_team_names:
                fantasy_team_names[int(i.attrs['href'].split('?teamId=')[1])] = str(i.contents[0])

        else:
            for i in league_home_team_names:
                fantasy_team_names[int(i.attrs['href'].split('/')[-1:][0])] = str(i.contents[0])

        return fantasy_team_names

    def create_team_rosters(self) -> dict:
        """Returns the active team roster or the end of season roster if param: season_end_year is used."""
        fantasy_team_names = self.get_fantasy_team_names()

        team_rosters = self.get_team_roster_by_team_id()
        fantasy_team_rosters = {}

        for i in team_rosters:
            fantasy_team_id = int(i[0].split('teamId=')[1])
            fantasy_team_name = fantasy_team_names[fantasy_team_id]
            for player in i[1]:
                player_id = int(player.attrs['href'].split('playerId=')[1])
                if str(player.contents[0]) != 'View News':
                    player_name = str(player.contents[0])
                    fantasy_team_rosters.update({player_id: {"PlayerName": player_name,
                                                             "FantasyTeamId": fantasy_team_id,
                                                             "FantasyTeamName": fantasy_team_name}})

        return fantasy_team_rosters
