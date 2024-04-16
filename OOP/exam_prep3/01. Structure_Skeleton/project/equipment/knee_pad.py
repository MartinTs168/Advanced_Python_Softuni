from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):

    def __init__(self):
        super().__init__(price=15.0, protection=120)

    def increase_price(self):
        self.price *= 1.2
