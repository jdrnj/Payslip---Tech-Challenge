import unittest
import pandas as pd
import os

class TestEmployeeMismatch(unittest.TestCase):
    def test_employees_missing_in_gtn(self):
        folder_path = '.'
        gtn_path = os.path.join(folder_path, 'GTN.xlsx')
        payrun_path = os.path.join(folder_path, 'Payrun.xlsx')

        try:
            gtn_df = pd.read_excel(gtn_path)
            payrun_df = pd.read_excel(payrun_path)
        except Exception as e:
            self.fail(f"Error reading Excel files: {e}")

        gtn_ids = set(gtn_df['employee_id'].dropna().astype(str))
        payrun_ids = set(payrun_df['Employee ID'].dropna().astype(str))

        missing = payrun_ids - gtn_ids

        if missing:
            self.fail(f"Employees present in Payrun but missing in GTN: {missing}")

if __name__ == '__main__':
    unittest.main()