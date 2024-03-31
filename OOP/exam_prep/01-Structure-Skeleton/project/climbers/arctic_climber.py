from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name):
        super().__init__(name, 200)

    @property
    def type(self):
        return "ArcticClimber"

    def can_climb(self):
        return True if self.strength >= 100 else False

    def climb(self, peak: BasePeak):
        strength_reduction = 2 if peak.difficulty_level == "Extreme" else 1.5
        strength_reduction *= 20
        self.strength -= strength_reduction
        self.conquered_peaks.append(peak.name)
