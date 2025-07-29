import unittest
import pandas as pd
import os

class TestStructure(unittest.TestCase):
    def test_file_structure(self):
        try:
            pd.read_excel('GTN.xlsx')
            pd.read_excel('Payrun.xlsx')
        except Exception as e:
            self.fail(f"Failed to load GTN or Payrun: {e}")

if __name__ == '__main__':
    unittest.main()
