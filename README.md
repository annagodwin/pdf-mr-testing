# pdf-mr-testing

A repo for housing tests for if a PDF is Machine Readable (the "MR" in pdf-mr-testing). 

Limitations: Currently tests "extracting text" from PDFs and not the extraction of other images/objects.

## Installation

Python 3.8.15 with dependencies in `requirements.txt`

## Example

```python pdfmrtesting/run_test.py 'pymupdf' 'data/pdf_dir_to_test' 'data/test_output'```

The `run_test.py` file has 3 required arguments:

- `reader`: the PDF reader to test extraction with (currently testing with `pymupdf`, `pypdf2` (pretty fast!) and `pdfplumber`, `pdfminersix` (slow!))
- `pdf_dir`: the directory containing PDFs to run the test against 
- `output_dir`: the directory to write the test results to

and has 2 outputs per run:

- the chosen `reader` argument saved as a `{reader}.csv` file in the output directory
    - each row in the CSV file contains the filename, the result of testing extracting text from the PDF (`Machine Readable`, `Needs OCR`, or Exception error encountered)
- Appends the duration for the reader to the `timing.csv` in the output directory

