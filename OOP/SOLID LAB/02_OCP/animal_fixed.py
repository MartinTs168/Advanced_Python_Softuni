from abc import ABC, abstractmethod


class Animal(ABC):
    def get_species(self):
        return self.__class__.__name__.lower()

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Chicken(Animal):
    def make_sound(self):
        return "kutkudqk"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat()]
animal_sound(animals)

animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
