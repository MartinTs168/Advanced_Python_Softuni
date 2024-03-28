from Advanced_and_OOP.OOP.design_patters.factory_ex.factories.abstract_factory import AbstractFactory
from Advanced_and_OOP.OOP.design_patters.factory_ex.furnitieres.chair import Chair
from Advanced_and_OOP.OOP.design_patters.factory_ex.furnitieres.sofa import Sofa
from Advanced_and_OOP.OOP.design_patters.factory_ex.furnitieres.table import Table


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair("Moder")

    def create_sofa(self):
        return Sofa("Moder")

    def create_table(self):
        return Table("Moder")
