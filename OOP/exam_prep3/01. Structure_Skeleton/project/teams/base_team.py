from abc import ABC, abstractmethod
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        ...

    @property
    def total_equipment_price(self):
        return sum([x.price for x in self.equipment])

    @property
    def avg_team_protection(self):
        return int(sum([x.protection for x in self.equipment]) / len(self.equipment)) if len(self.equipment) > 0 else 0

    def total_team_protection(self):
        return sum([x.protection for x in self.equipment])

    @property
    def type(self):
        return self.__class__.__name__

    def get_statistics(self):
        return (
            f"Name: {self.name}\n"
            f"Country: {self.country}\n"
            f"Advantage: {self.advantage} points\n"
            f"Budget: {self.budget:.2f}EUR\n"
            f"Wins: {self.wins}\n"
            f"Total Equipment Price: {self.total_equipment_price:.2f}\n"
            f"Average Protection: {self.avg_team_protection}"
        )