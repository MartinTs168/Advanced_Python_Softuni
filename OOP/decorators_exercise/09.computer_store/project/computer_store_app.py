from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    __VALID_COMPUTER_TYPES = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop,
    }

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        try:
            computer = self.__VALID_COMPUTER_TYPES[type_computer](manufacturer, model)
        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration_message = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return configuration_message

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget \
                    and computer.processor == wanted_processor \
                    and computer.ram >= wanted_ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")
