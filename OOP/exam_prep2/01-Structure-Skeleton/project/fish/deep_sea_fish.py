from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    __TIME_TO_CATCH = 180

    def __init__(self, name, points):
        super().__init__(name, points, self.__TIME_TO_CATCH)

    @property
    def type(self):
        return "DeepSeaFish"




