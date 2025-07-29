import unittest
import pandas as pd
import os
import json

class TestUnmappedGTNElements(unittest.TestCase):
    def test_unmapped_elements_in_gtn(self):
        folder_path = '.'
        gtn_path = os.path.join(folder_path, 'GTN.xlsx')
        mapping_path = os.path.join(folder_path, 'mapping.json')

        try:
            gtn_df = pd.read_excel(gtn_path)
            with open(mapping_path, 'r') as f:
                mapping = json.load(f)
        except Exception as e:
            self.fail(f"Error reading GTN or mapping file: {e}")

        gtn_elements = gtn_df.columns[4:]

        mapped_vendors = set(
            v['vendor'] for v in mapping.get('mappings', {}).values() if v.get('map') == True
        )

        unmapped = [elem for elem in gtn_elements if elem not in mapped_vendors]

        if unmapped:
            self.fail(f"GTN has unmapped pay elements: {unmapped}")

if __name__ == '__main__':
    unittest.main()