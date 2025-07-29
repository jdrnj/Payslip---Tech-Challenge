import unittest
import pandas as pd

class TestRequiredColumns(unittest.TestCase):
    def test_columns_exist(self):
        gtn = pd.read_excel('GTN.xlsx')
        payrun = pd.read_excel('Payrun.xlsx')
        
        self.assertIn('employee_id', gtn.columns)
        self.assertIn('Employee ID', payrun.columns)

if __name__ == '__main__':
    unittest.main()