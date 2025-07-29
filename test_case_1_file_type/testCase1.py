import os
import pandas as pd

def test_file_is_excel():
    folder_path = "tests/test_case_1_file_type"
    
    gtn_path = os.path.join(folder_path, "GTN.xlsx")
    payrun_path = os.path.join(folder_path, "Payrun.xlsx")

    try:
        pd.read_excel(gtn_path)
    except Exception as e:
        assert False, f"GTN.xlsx is not a valid Excel file. Error: {e}"

    try:
        pd.read_excel(payrun_path)
    except Exception as e:
        assert False, f"Payrun.xlsx is not a valid Excel file. Error: {e}"
