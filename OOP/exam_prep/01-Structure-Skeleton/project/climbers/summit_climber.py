from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name):
        super().__init__(name, 150)

    @property
    def type(self):
        return "SummitClimber"

    def can_climb(self):
        return True if self.strength >= 75 else False

    def climb(self, peak: BasePeak):
        strength_reduction = 1.3 if peak.difficulty_level == "Advanced" else 2.5
        strength_reduction *= 30
        self.strength -= strength_reduction
        self.conquered_peaks.append(peak.name)