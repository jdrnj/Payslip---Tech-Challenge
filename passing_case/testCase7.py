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

        gtn_elements = [
            col for col in gtn_df.columns[4:]
            if not col.startswith("Unnamed")
        ]

        mapped_vendors = set()
        for v in mapping.get("mappings", {}).values():
            if v.get("map", False) and "vendor" in v:
                mapped_vendors.add(v["vendor"])

        not_used_vendors = {
            item.get("vendor") for item in mapping.get("not_used", [])
            if "vendor" in item
        }

        allowed_vendors = mapped_vendors.union(not_used_vendors)

        unmapped = [col for col in gtn_elements if col not in allowed_vendors]

        if unmapped:
            self.fail(f"GTN has unmapped pay elements: {unmapped}")

if __name__ == '__main__':
    unittest.main()
