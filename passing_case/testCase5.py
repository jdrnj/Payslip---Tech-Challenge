import unittest
import pandas as pd
import os

class TestEmployeeMismatchReverse(unittest.TestCase):
    def test_employees_missing_in_payrun(self):
        folder_path = '.'
        gtn_path = os.path.join(folder_path, 'GTN.xlsx')
        payrun_path = os.path.join(folder_path, 'Payrun.xlsx')

        try:
            gtn_df = pd.read_excel(gtn_path)
            payrun_df = pd.read_excel(payrun_path)
        except Exception as e:
            self.fail(f"Error reading Excel files: {e}")

        gtn_ids = set(
            gtn_df['employee_id']
            .dropna()
            .apply(lambda x: str(int(float(x))) if pd.notnull(x) else None)
        )

        payrun_ids = set(
            payrun_df['Employee ID']
            .dropna()
            .apply(lambda x: str(int(float(x))) if pd.notnull(x) else None)
        )

        missing = gtn_ids - payrun_ids

        if missing:
            self.fail(f"Employees in GTN but missing in Payrun: {missing}")

if __name__ == '__main__':
    unittest.main()
