# PDF Modification Script with PyMuPDF

This script modifies a PDF check by clearing specific text areas and inserting updated values. It is designed to be simple and user-friendly, with configurations managed via a JSON file.

## Prerequisites
To run this script, ensure you have the following:

1. **Python 3.8+**
   - Download Python: [https://www.python.org/](https://www.python.org/)

2. **Virtual Environment** (recommended)
   - Use `venv` to isolate the dependencies for the project.

3. Required Python Packages:
   - `PyMuPDF` (fitz) for PDF manipulation

4. **Original PDF File**
   - Place the PDF file you want to modify in the project folder.

5. **Configuration JSON**
   - A JSON file that contains the values to replace in the PDF.

---

## Installation and Setup

### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Set up Virtual Environment
Create a virtual environment to keep dependencies isolated.
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate   # For Windows
```

### Step 3: Install Dependencies
Install the required libraries from `requirements.txt`.
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install `PyMuPDF` manually:
```bash
pip install PyMuPDF
```

### Step 4: JSON Configuration
Create a `values.json` file in the project directory with the following structure:

```json
{
  "payee_name": "John Doe",
  "amount": "20,000 Bonusly Points",
  "amount_words": "Twenty Thousand Bonusly Points Only",
  "check_number": "0032",
  "date": "2024-12-19",
  "memo": "Recognition Bonus"
}
```
- **payee_name**: The recipient's name.
- **amount**: The numerical value of the amount.
- **amount_words**: The amount written in words.
- **check_number**: The check number displayed.
- **date**: Date in `YYYY-MM-DD` format.
- **memo**: Additional note for the check.

---

## Script Usage

### Input PDF File
Ensure you have the original PDF file (e.g., `original_check.pdf`) in the project folder.

### Run the Script
Execute the script to generate a modified PDF:
```bash
python script.py
```

The script will:
1. Load the configuration from `values.json`.
2. Modify specific areas of the PDF based on the JSON values.
3. Save the output PDF with a dynamic name based on the JSON file name and the `payee_name`.

### Output File Naming
The output file will be named dynamically as:
```bash
<json_filename>-<payee_name>.pdf
```
For example, if your JSON file is `values.json` and `payee_name` is `John Doe`, the output file will be:
```
values-john-doe.pdf
```

---

## How It Works
1. **Text Clearing**:
   - The script clears predefined areas of the PDF to remove existing text.

2. **Text Insertion**:
   - New text is inserted into the cleared areas based on the configuration.
   - Bold text is supported using the built-in `helvetica-bold` font.

3. **Dynamic File Generation**:
   - The output file name is generated dynamically based on the JSON file name and payee name.

---

## Troubleshooting
1. **Font Errors**:
   - If the font `helvetica-bold` is unavailable, ensure PyMuPDF is properly installed.

2. **File Not Found**:
   - Ensure the input PDF file exists in the specified location.

3. **Dependencies**:
   - Reinstall PyMuPDF:
     ```bash
     pip install --force-reinstall PyMuPDF
     ```

4. **JSON Errors**:
   - Verify the JSON file follows correct syntax.

---

## Output Example
The modified PDF will have the updated text with correct formatting, such as:
- Payee Name: `John Doe`
- Amount: `20,000 Bonusly Points`
- Date: `2024-12-19`
- Memo: `Recognition Bonus`

The output file name will be:
```
values-john-doe.pdf
```

---

## Contact
For any issues, please reach out to the project maintainer.
