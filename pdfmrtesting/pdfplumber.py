import pdfplumber
from pathlib import Path
from utils import determine_result


def test_extract_text(pdf_filepath: Path): 

    try:
        pdf = pdfplumber.open(pdf_filepath)

        text_list = list()
        for page in pdf.pages:
            text_list.append(page.extract_text())

        text = "".join(text_list).strip()
        result = determine_result(text)
    
    except Exception as e:
        result = e
    
    return result