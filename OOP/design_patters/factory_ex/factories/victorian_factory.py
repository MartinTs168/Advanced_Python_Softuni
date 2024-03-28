from Advanced_and_OOP.OOP.design_patters.factory_ex.factories.abstract_factory import AbstractFactory
from Advanced_and_OOP.OOP.design_patters.factory_ex.furnitieres.chair import Chair
from Advanced_and_OOP.OOP.design_patters.factory_ex.furnitieres.sofa import Sofa
from Advanced_and_OOP.OOP.design_patters.factory_ex.furnitieres.table import Table


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Sofa("Victorian")

    def create_sofa(self):
        return Chair("Victorian")

    def create_table(self):
        return Table("Victorian")
