from typing import Dict

from project.computer_types.computer import Computer


class Laptop(Computer):
    @property
    def type(self) -> str:
        return "laptop"

    @property
    def max_ram(self) -> int:
        return 64

    @property
    def available_processors(self) -> Dict[str, int]:
        processor_prices = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

        return processor_prices
