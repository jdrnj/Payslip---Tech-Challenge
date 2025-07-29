import unittest
import pandas as pd

class TestGTNHeaderStructure(unittest.TestCase):
    def test_extra_header_row_in_gtn(self):
        df_preview = pd.read_excel('GTN.xlsx', nrows=5, header=None)
        string_row_counts = df_preview.apply(lambda row: row.map(lambda x: isinstance(x, str))).sum(axis=1)
        header_row_index = string_row_counts.idxmax()

        if header_row_index > 0:
            self.fail(f"Extra header row detected at index {header_row_index}")

if __name__ == '__main__':
    unittest.main()