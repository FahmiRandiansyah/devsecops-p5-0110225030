class FinancialCalculator:
    def calculate_roi(self, net_profit: float, investment: float) -> float:
        if investment <= 0:
            raise ValueError("Investment must be greater than zero.")
        return (net_profit / investment) * 100

    def calculate_tax(self, income: float, tax_rate: float) -> float:
        if income < 0 or tax_rate < 0:
            raise ValueError("Income and tax rate cannot be negative.")
        return income * (tax_rate / 100)