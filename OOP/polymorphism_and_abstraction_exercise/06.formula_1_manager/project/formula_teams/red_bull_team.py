from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    @property
    def expenses(self):
        return 250_000

    @property
    def sponsors(self):
        return [{1: 1_500_000, 2: 800_000}, {8: 20_000, 10: 10_000}]
