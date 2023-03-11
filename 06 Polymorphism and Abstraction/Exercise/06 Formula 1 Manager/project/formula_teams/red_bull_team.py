from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES = 250000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        # calculate revenue from sponsor Oracle:
        if race_pos == 1:
            revenue += 1500000
        elif race_pos == 2:
            revenue += 800000

        # calculate revenue from sponsor Honda:
        if race_pos <= 8:
            revenue += 20000
        elif race_pos <= 10:
            revenue += 10000

        revenue -= RedBullTeam.EXPENSES
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
