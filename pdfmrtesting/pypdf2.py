from PyPDF2 import PdfReader
from utils import determine_result
from pathlib import Path


def test_extract_text(pdf_filepath: Path) -> str:
    """Tests the extract text functionality of the PDF reader

    Args:
        pdf_filepath (Path): PDF filepath

    Returns:
        str: Returns "Machine Readable", "Needs OCR", or the exception string
    """

    try: 
        reader = PdfReader(pdf_filepath)

        text_list = list()
        for i in range(0,len(reader.pages)):
            page = reader.pages[i]
            page_text = page.extract_text()
            text_list.append(page_text)

        text = "".join(text_list).strip()
        
        result = determine_result(text)
        
    except Exception as e:
        result = e
    
    return result