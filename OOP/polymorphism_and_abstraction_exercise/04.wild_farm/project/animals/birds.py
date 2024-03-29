from typing import List, Type

from project.animals.animal import Bird
from project.food import Seed, Meat, Vegetable, Fruit


class Owl(Bird):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
