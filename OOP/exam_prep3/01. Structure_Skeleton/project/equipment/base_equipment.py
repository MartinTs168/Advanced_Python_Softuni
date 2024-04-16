from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, price, protection):
        self.price = price
        self.protection = protection

    @abstractmethod
    def increase_price(self):
        ...

    @property
    def type(self):
        return self.__class__.__name__
