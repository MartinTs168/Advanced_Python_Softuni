from abc import ABC, abstractmethod
from math import log2
from typing import Dict


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str, ):
        self.model = model
        self.manufacturer = manufacturer
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @property
    @abstractmethod
    def max_ram(self) -> int:
        ...

    @property
    @abstractmethod
    def available_processors(self) -> Dict[str, int]:
        ...

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @staticmethod
    def power_of_2(ram: int):
        result = log2(ram)
        return result.is_integer()

    def set_parts(self, processor, ram):
        self.processor = processor
        self.ram = ram
        processor_price = self.available_processors[processor]
        ram_price = 100 * log2(ram)
        self.price = processor_price + int(ram_price)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if ram > self.max_ram or not self.power_of_2(ram):
            raise ValueError(
                f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
