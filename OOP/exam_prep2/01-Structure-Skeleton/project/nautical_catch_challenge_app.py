from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver

from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    __VALID_DIVER_TYPES = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver,
    }

    __VALID_FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            diver = self.__VALID_DIVER_TYPES[diver_type](diver_name)
            next(filter(lambda d: d.name == diver_name, self.divers))
        except KeyError:
            return f"{diver_type} is not allowed in our competition."
        except StopIteration:  # positive case
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

        return f"{diver_name} is already a participant."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        try:
            fish = self.__VALID_FISH_TYPES[fish_type](fish_name, points)
            next(filter(lambda f: f.name == fish_name, self.fish_list))
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."
        except StopIteration:  # positive case
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

        return f"{fish_name} is already permitted."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        message = ''

        if diver.has_health_issues:
            message = f"{diver_name} will not be allowed to dive, due to health issues."

        elif diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish)
                message = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.has_health_issues = True

        return message

    def health_recovery(self):
        counter = 0
        for diver in self.divers:
            if diver.has_health_issues:
                diver.update_health_status()
                diver.renew_oxy()
                counter += 1
        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        return f"**{diver_name} Catch Report**\n" + \
            "\n".join(f.fish_details() for f in diver.catch)

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if not d.has_health_issues]
        healthy_divers.sort(key=lambda x: (-x.competition_points, -len(x.catch), x.name))

        return f"**Nautical Catch Challenge Statistics**\n" + \
            "\n".join(str(d) for d in healthy_divers)
