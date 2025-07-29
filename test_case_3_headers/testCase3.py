import unittest
import pandas as pd
import os

class TestGTNHeaderStructure(unittest.TestCase):
    def test_extra_header_row_in_gtn(self):
        folder_path = '.'
        gtn_path = os.path.join(folder_path, 'GTN.xlsx')

        try:
            df_preview = pd.read_excel(gtn_path, nrows=5, header=None)
        except Exception as e:
            self.fail(f"Could not read GTN.xlsx: {e}")

        string_row_counts = df_preview.applymap(lambda x: isinstance(x, str)).sum(axis=1)
        
        probable_headers = string_row_counts[string_row_counts > len(df_preview.columns) / 2]

        if len(probable_headers) > 1:
            self.fail(f"GTN.xlsx may have extra header rows: {probable_headers.index.tolist()}")

if __name__ == '__main__':
    unittest.main()