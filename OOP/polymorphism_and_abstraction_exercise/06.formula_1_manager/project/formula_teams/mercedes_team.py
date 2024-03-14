from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    @property
    def expenses(self):
        return 200_000

    @property
    def sponsors(self):
        return [{1: 1_000_000, 3: 500_000}, {5: 100_000, 7: 50_000}]