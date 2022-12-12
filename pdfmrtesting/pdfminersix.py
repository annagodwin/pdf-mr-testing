from pdfminer.high_level import extract_text
from pathlib import Path
from utils import determine_result


def test_extract_text(pdf_filepath):
    try:
        text = extract_text(pdf_filepath).strip()
        
        result = determine_result(text)
        
    except Exception as e:
        result = e
    return result
    