import unittest
import pandas as pd
import os
import json

class TestGTNNumericValues(unittest.TestCase):
    def test_gtn_values_are_numeric(self):
        folder_path = '.'
        gtn_path = os.path.join(folder_path, 'GTN.xlsx')
        mapping_path = os.path.join(folder_path, 'mapping.json')

        try:
            gtn_df = pd.read_excel(gtn_path)
            with open(mapping_path, 'r') as f:
                mapping = json.load(f)
        except Exception as e:
            self.fail(f"Error reading GTN or mapping: {e}")

        # Get mapped pay elements (i.e. vendor fields)
        mapped_vendors = [
            v['vendor'] for v in mapping.get('mappings', {}).values() if v.get('map') == True
        ]

        non_numeric_entries = {}

        for col in mapped_vendors:
            if col in gtn_df.columns:
                # Convert to numeric and check which fail
                numeric_series = pd.to_numeric(gtn_df[col], errors='coerce')
                invalid = gtn_df[~numeric_series.notna()]

                if not invalid.empty:
                    non_numeric_entries[col] = invalid.index.tolist()

        if non_numeric_entries:
            self.fail(f"Non-numeric values found in mapped GTN pay elements: {non_numeric_entries}")

if __name__ == '__main__':
    unittest.main()
