from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    __OXYGEN_LEVEL = 120

    def __init__(self, name):
        super().__init__(name, self.__OXYGEN_LEVEL)

    @property
    def type(self):
        return "FreeDiver"

    def miss(self, time_to_catch):
        reduce_amount = round(0.6 * time_to_catch)

        if self.oxygen_level < reduce_amount:
            self.oxygen_level = 0

        else:
            self.oxygen_level -= reduce_amount

    def renew_oxy(self):
        self.oxygen_level = self.__OXYGEN_LEVEL
