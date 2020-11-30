import unittest
import Calculator
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator.Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator.Calculator)

    def test_addition_calculator(self):
        test_data = CSVReader("src/Tests/Addition.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction_calculator(self):
        test_data = CSVReader("src/Tests/Subtraction.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication_calculator(self):
        test_data = CSVReader("src/Tests/Multiplication.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division_calculator(self):
        test_data = CSVReader("src/Tests/Division.csv").data
        for row in test_data:
            result = round(float(row['Result']), 7)
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()