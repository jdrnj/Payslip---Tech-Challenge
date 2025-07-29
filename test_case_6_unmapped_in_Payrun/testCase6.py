import unittest
import pandas as pd
import os
import json

class TestUnmappedPayElementsInPayrun(unittest.TestCase):
    def test_unmapped_elements_in_payrun(self):
        folder_path = '.'
        payrun_path = os.path.join(folder_path, 'Payrun.xlsx')
        mapping_path = os.path.join(folder_path, 'mapping.json')

        try:
            payrun_df = pd.read_excel(payrun_path)
            with open(mapping_path, 'r') as f:
                mapping = json.load(f)
        except Exception as e:
            self.fail(f"Error reading Payrun or mapping file: {e}")

        payrun_elements = payrun_df.columns[25:]

        mapped_elements = set(mapping["mappings"].keys())

        unmapped = [elem for elem in payrun_elements if elem not in mapped_elements]

        if unmapped:
            self.fail(f"Payrun has unmapped pay elements: {unmapped}")

if __name__ == '__main__':
    unittest.main()