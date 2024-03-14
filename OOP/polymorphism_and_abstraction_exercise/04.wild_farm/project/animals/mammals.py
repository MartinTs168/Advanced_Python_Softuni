from typing import List, Type

from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    @property
    def food_that_eats(self) :
        return [Fruit, Vegetable]

    def make_sound(self):
        return "Squeak"

    @property
    def gained_weight(self):
        return 0.10


class Tiger(Mammal):
    @property
    def food_that_eats(self) :
        return [Meat]

    def make_sound(self):
        return "ROAR!!!"

    @property
    def gained_weight(self):
        return 1


class Dog(Mammal):

    @property
    def food_that_eats(self) :
        return [Meat]

    @property
    def gained_weight(self):
        return 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    def make_sound(self):
        return "Meow"

    @property
    def gained_weight(self):
        return 0.3
