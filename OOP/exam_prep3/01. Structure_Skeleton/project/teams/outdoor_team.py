from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, 1000.0)

    def win(self):
        self.wins += 1
        self.advantage += 115
