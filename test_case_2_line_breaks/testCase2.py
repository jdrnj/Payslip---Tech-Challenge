import unittest
import pandas as pd
import os

class TestGTNLineBreaks(unittest.TestCase):
    def test_empty_rows_in_gtn(self):
        folder_path = 'tests/test_case_2_line_breaks'
        gtn_path = os.path.join(folder_path, 'GTN.xlsx')

        try:
            df = pd.read_excel(gtn_path)
        except Exception as e:
            self.fail(f"Could not read GTN.xlsx: {e}")

        empty_rows = df[df.isnull().all(axis=1)]

        if not empty_rows.empty:
            self.fail(f"GTN.xlsx contains empty rows at indexes: {empty_rows.index.tolist()}")

if __name__ == '__main__':
    unittest.main()