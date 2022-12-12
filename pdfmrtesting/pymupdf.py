import fitz
from pathlib import Path
from utils import determine_result


def test_extract_text(pdf_filepath: Path): 

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