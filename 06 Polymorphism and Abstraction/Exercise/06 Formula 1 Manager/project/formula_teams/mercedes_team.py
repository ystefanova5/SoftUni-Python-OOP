from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES = 200000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        # calculate revenue from sponsor Petronas:
        if race_pos == 1:
            revenue += 1000000
        elif race_pos <= 3:
            revenue += 500000

        # calculate revenue from sponsor TeamViewer:
        if race_pos <= 5:
            revenue += 100000
        elif race_pos <= 7:
            revenue += 50000

        revenue -= MercedesTeam.EXPENSES
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
