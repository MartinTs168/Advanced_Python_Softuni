from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        ...

    @abstractmethod
    def create_sofa(self):
        ...

    @abstractmethod
    def create_table(self):
        ... 