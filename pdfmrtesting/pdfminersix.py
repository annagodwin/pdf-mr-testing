from pdfminer.high_level import extract_text
from pathlib import Path
from typing import Union
from utils import determine_result


def test_extract_text(pdf_filepath: Path) -> str:
    """Tests the extract text functionality of the PDF reader

    Args:
        pdf_filepath (Path): PDF filepath

    Returns:
        str: Returns "Machine Readable", "Needs OCR", or the exception string
    """

    try:
        text = extract_text(pdf_filepath).strip()
        
        result = determine_result(text)

    except Exception as e:
        result = e
    return result
    