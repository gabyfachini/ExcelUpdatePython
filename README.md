## Excel Cleaner - Remove "\_x000D\_" from Excel Files

This project is a Python script that reads an Excel file and replaces all occurrences of \_x000D\_ with a space, maintaining the spreadsheet structure.

---

### 🚀 How to Install Python

1. Download Python from the official website:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. During installation, **check the box that says "Add Python to PATH"**.

3. Complete the installation.

---

### 📦 Install Required Libraries

Open your terminal (Command Prompt, PowerShell, or terminal in VSCode) and run:
  
  `pip install pandas openpyxl`

If pip doesn't work, try:

  `python -m pip install --upgrade pip`
  
  `python -m pip install pandas openpyxl`

---

### ▶️ How to Run the Script
1. Save the script file as UpdateExcel.py.
2. Place the Excel file you want to process in the same folder as the script.
3. Open the terminal and navigate to the folder: 

    `cd C:\Users\YourName\Path\To\Your\Folder`

4. Run the script with:

    `python UpdateExcel.py`

5. A new Excel file named `cleaned_spreadsheet.xlsx` will be created in the same folder. You can rename the output file directly in the Python script if desired.

6. **WARNING**: If you've already created an output file and run the script again, it will overwrite the existing `cleaned_spreadsheet.xlsx`. To create a new output file instead, you must change the output filename in the script manually.

