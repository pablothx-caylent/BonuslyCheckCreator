import fitz  # PyMuPDF
import json
import os

# Configuration - Users can modify these fields in the input JSON file
CONFIG_FILE = "values.json"
INPUT_PDF = "original_check.pdf"  # Original PDF path
OUTPUT_PDF = "check_corrected.pdf"  # New PDF path


def load_config(config_file):
    """
    Load configuration from a JSON file.
    :param config_file: Path to the JSON configuration file
    :return: Dictionary with configuration values
    """
    with open(config_file, "r") as file:
        return json.load(file)


def clear_and_insert_text(page, x, y, width, height, text, font_size, color, fontname="helvetica-bold"):
    """
    Clear an area and insert bold text into the PDF page.
    :param page: The PDF page object
    :param x: X coordinate for clearing and text insertion
    :param y: Y coordinate for clearing and text insertion
    :param width: Width of the area to clear
    :param height: Height of the area to clear
    :param text: The text to insert
    :param font_size: Font size for the text
    :param color: Text color (RGB tuple)
    :param fontname: Standard font name (e.g., 'helvetica-bold' for Helvetica Bold)
    """
    rect = fitz.Rect(x, y, x + width, y + height)
    page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))  # Clear area
    page.insert_text((x, y + font_size - 2), text,
                     fontsize=font_size, color=color, fontname=fontname)




def modify_pdf(input_pdf, output_pdf, config):
    """
    Function to modify a PDF check using PyMuPDF.
    :param input_pdf: Path to the original PDF
    :param output_pdf: Path to save the modified PDF
    :param config: Dictionary with configuration values
    """
    # Open the original PDF
    pdf = fitz.open(input_pdf)
    page = pdf[0]  # Assuming the check content is on the first page

    # Define text properties
    font_size = 14
    color = (0, 0, 0)  # Black

    # Clear areas and insert updated text
    clear_and_insert_text(page, 167, 176, 200, 20, config.get(
        "payee_name", ""), font_size, color, fontname="helvetica-bold")  # Payee Name
    clear_and_insert_text(page, 330, 223, 200, 20, config.get(
        "amount", ""), 18, color)       # Amount
    clear_and_insert_text(page, 130, 277, 200, 20, config.get(
        "amount_words", ""), 12, color, fontname="helvetica")  # Amount Words
    clear_and_insert_text(page, 788, 44, 70, 20, config.get(
        "check_number", ""), 10, color, fontname="helvetica")   # Check Number
    clear_and_insert_text(page, 63, 320, 200, 20, config.get(
        "date", ""), 12, color, fontname="helvetica")         # Date
    clear_and_insert_text(page, 72, 362, 200, 20, config.get(
        "memo", ""), 12, color, fontname="helvetica")         # Memo

    # Save the modified PDF
    pdf.save(output_pdf)
    pdf.close()
    print(f"Check successfully modified and saved as '{output_pdf}'.")


def generate_output_filename(config_file, config):
    """
    Generate output PDF file name based on the JSON file and payee name.
    :param config_file: Path to the configuration JSON file
    :param config: Dictionary with configuration values
    :return: Generated output file name
    """
    json_name = os.path.splitext(os.path.basename(config_file))[0]
    payee_name = config.get("payee_name", "output").lower().replace(" ", "-")
    return f"{json_name}-{payee_name}.pdf"

if __name__ == "__main__":
    print("Loading configuration from JSON file...")
    config = load_config(CONFIG_FILE)
    OUTPUT_PDF = generate_output_filename(CONFIG_FILE, config)
    print("Modifying the check PDF...")
    modify_pdf(INPUT_PDF, OUTPUT_PDF, config)
