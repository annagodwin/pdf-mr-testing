import fitz
from pathlib import Path
from utils import determine_result


def test_extract_text(pdf_filepath: Path) -> str:
    """Tests the extract text functionality of the PDF reader

    Args:
        pdf_filepath (Path): PDF filepath

    Returns:
        str: Returns "Machine Readable", "Needs OCR", or the exception string
    """

    try: 
        doc = fitz.open(pdf_filepath)

        text_list = list()
        for page in doc:
                text_list.append(page.get_textpage().extractText())

        text = "".join(text_list).strip()
        result = determine_result(text)

    except Exception as e:
        result = e
    
    return result