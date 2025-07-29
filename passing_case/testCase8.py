import unittest
import pandas as pd
import json

class TestGTNNumericValues(unittest.TestCase):
    def test_gtn_values_are_numeric(self):
        gtn = pd.read_excel('GTN.xlsx')
        with open('mapping.json') as f:
            mapping = json.load(f)

        mapped_vendors = [
            v["vendor"] for v in mapping["mappings"].values() if v["map"] == True
        ]

        non_numeric = {}

        for col in mapped_vendors:
            if col in gtn.columns:
                series = pd.to_numeric(gtn[col], errors="coerce")
                invalid_rows = gtn[~series.notna()]
                if not invalid_rows.empty:
                    non_numeric[col] = [i + 2 for i in invalid_rows.index.tolist()]

        if non_numeric:
            self.fail(f"Non-numeric values found in GTN: {non_numeric}")

if __name__ == '__main__':
    unittest.main()