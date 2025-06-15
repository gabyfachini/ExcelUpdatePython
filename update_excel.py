import pandas as pd

# File path
file = 'test.xlsx'

# Read all sheets from the Excel file (if you want only one, use sheet_name='SheetName')
sheets = pd.read_excel(file, sheet_name=None)

# Create a dictionary to store the cleaned DataFrames
cleaned_sheets = {}

# Loop through each sheet
for sheet_name, df in sheets.items():
    # Apply the replacement to all cells that are text (object)
    cleaned_df = df.applymap(lambda x: x.replace('_x000D_', ' ') if isinstance(x, str) else x)
    cleaned_sheets[sheet_name] = cleaned_df

# Save the new Excel file with the changes
with pd.ExcelWriter('cleaned_spreadsheet.xlsx', engine='openpyxl') as writer:
    for sheet_name, df in cleaned_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Replacement completed. File saved as 'cleaned_spreadsheet.xlsx'.")
# Note: Ensure you have the required libraries installed
# by running: pip install pandas openpyxl