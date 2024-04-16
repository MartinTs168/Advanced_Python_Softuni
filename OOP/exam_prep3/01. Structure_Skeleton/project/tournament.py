from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    __VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    __VALID_TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            equipment = self.__VALID_EQUIPMENT_TYPES[equipment_type]()
            self.equipment.append(equipment)
            return f"{equipment_type} was successfully added."
        except KeyError:
            raise ValueError("Invalid equipment type!")

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.__VALID_TEAM_TYPES[team_type](team_name, country, advantage)
            if not self.capacity > 0:
                return "Not enough tournament capacity."
            self.teams.append(team)
            self.capacity -= 1
            return f"{team_type} was successfully added."
        except KeyError:
            raise ValueError("Invalid team type!")

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = next(filter(lambda x: x.type == equipment_type, self.equipment.__reversed__()))
        team = next(filter(lambda x: x.name == team_name, self.teams))
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        team.budget -= equipment.price
        team.equipment.append(equipment)
        self.equipment.remove(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda x: x.name == team_name, self.teams))
            if team.wins > 0:
                return f"The team has {team.wins} wins! Removal is impossible!"
            self.teams.remove(team)
            self.capacity += 1
            return f"Successfully removed {team_name}."
        except StopIteration:
            raise ValueError("No such team!")

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for eq in self.equipment:
            if eq.type == equipment_type:
                count += 1
                eq.increase_price()
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1, team_name2):
        team1 = next(filter(lambda x: x.name == team_name1, self.teams))
        team2 = next(filter(lambda x: x.name == team_name2, self.teams))
        if team1.type != team2.type:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_score = team1.advantage + team1.total_team_protection()
        team2_score = team2.advantage + team2.total_team_protection()

        if team1_score == team2_score:
            return "No winner in this game."
        if team1_score > team2_score:
            team1.win()
            return f"The winner is {team1.name}."
        if team1_score < team2_score:
            team2.win()
            return f"The winner is {team2.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        return (f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n" +
                "\n".join([x.get_statistics() for x in sorted_teams]))
