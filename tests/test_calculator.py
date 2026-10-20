import unittest
from src.calculator import FinancialCalculator

class TestFinancialCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = FinancialCalculator()

    def test_calculate_roi(self):
        result = self.calc.calculate_roi(100, 500)
        self.assertEqual(result, 20.0)

    def test_calculate_tax(self):
        result = self.calc.calculate_tax(1000, 10)
        self.assertEqual(result, 100.0)

if __name__ == '__main__':
    unittest.main()