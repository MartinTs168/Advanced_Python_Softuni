from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    __STRENGTH_INCREASE = 15

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")

        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @property
    @abstractmethod
    def type(self):
        ...

    @abstractmethod
    def can_climb(self):
        ...

    @abstractmethod
    def climb(self, peak: BasePeak):
        ...

    def rest(self):
        self.strength += self.__STRENGTH_INCREASE

    def __str__(self):
        conquered_peaks = ", ".join(sorted(self.conquered_peaks))
        return (f"{self.type}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * "
                f"Conquered peaks: {conquered_peaks} ///")
