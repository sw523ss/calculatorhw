import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 6)

    def test_subtraction_method_calculator(self):
        test_data = CsvReader("/CSVFiles/Unit_Test_Subtraction.csv").data

        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 6)

    if __name__ == '__main__':
        unittest.main()