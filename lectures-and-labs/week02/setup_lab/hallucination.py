import pandas as pd


def load_spreadsheet(file_path: str) -> pd.DataFrame:
    """Load a spreadsheet from the given file path."""
    return pd.read_excel(file_path)


spreadsheet = load_spreadsheet("data.xlsx")
print(spreadsheet)