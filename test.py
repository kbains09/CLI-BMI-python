import unittest
from main import calculate_bmi, interpret_bmi

class TestBMICalculator(unittest.TestCase):

    def test_normal_case(self):
        self.assertAlmostEqual(calculate_bmi(150, 5, 7), 23.49, places=2)
        self.assertEqual(interpret_bmi(23.49), "Normal weight")

    def test_underweight_case(self):
        self.assertAlmostEqual(calculate_bmi(100, 6, 0), 13.56, places=2)  # Updated expected value
        self.assertEqual(interpret_bmi(13.56), "Underweight")

    def test_overweight_case(self):
        self.assertAlmostEqual(calculate_bmi(200, 5, 5), 33.28, places=2)  # Updated expected value
        self.assertEqual(interpret_bmi(33.28), "Overweight")


if __name__ == '__main__':
    unittest.main()
