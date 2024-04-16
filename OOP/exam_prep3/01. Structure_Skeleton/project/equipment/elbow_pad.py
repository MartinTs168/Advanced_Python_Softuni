from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):

    def __init__(self):
        super().__init__(price=25.0, protection=90)

    def increase_price(self):
        self.price *= 1.1
