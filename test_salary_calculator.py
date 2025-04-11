import unittest
from salary_calculator import calculate_salary


class TestSalaryCalculator(unittest.TestCase):
    def test_salary_calculation(self):
        # Test case 1: Normal scenario
        gross, net = calculate_salary(40, 25, 100)
        self.assertEqual(gross, 1000)
        self.assertEqual(net, 900)

        # Test case 2: No deductions
        gross, net = calculate_salary(40, 25, 0)
        self.assertEqual(gross, 1000)
        self.assertEqual(net, 1000)

        # Test case 3: Zero hours worked
        gross, net = calculate_salary(0, 25, 100)
        self.assertEqual(gross, 0)
        self.assertEqual(net, 0)

        # Test case 4: Deductions exceed gross salary
        gross, net = calculate_salary(40, 25, 1200)
        self.assertEqual(gross, 1000)
        self.assertEqual(net, 0)


if __name__ == '__main__':
    unittest.main()
    