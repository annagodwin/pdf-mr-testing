from pdfminer.high_level import extract_text
from pathlib import Path
from utils import determine_result, timeout

@timeout(5)
def lib_extract_text(pdf_filepath: Path): 

    try:
        text = extract_text(pdf_filepath).strip()
        
        result = determine_result(text)
    
    except Exception as e:
        result = e
    
    return result

def test_extract_text(pdf_filepath):
    try:
        result = lib_extract_text(pdf_filepath)
    except Exception as e:
        result = e
    return result
    