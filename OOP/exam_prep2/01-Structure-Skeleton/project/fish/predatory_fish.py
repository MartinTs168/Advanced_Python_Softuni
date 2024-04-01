from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):

    __TIME_TO_CATCH = 90

    def __init__(self, name, points):
        super().__init__(name, points, self.__TIME_TO_CATCH)

    @property
    def type(self):
        return "PredatoryFish"




