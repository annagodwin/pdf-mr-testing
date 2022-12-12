import argparse
import os
from pathlib import Path
import csv
import time
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("reader", type=str,
                        help="PDF reader library", 
                        choices=['pymupdf', 'pdfminersix', 'pypdf2', 'pdfplumber'])
    parser.add_argument("pdf_dir", type=Path,
                        help="Directory containing PDFs for testing")
    parser.add_argument("output_dir", type=Path,
                        help="Directory containing testing results")
    args = parser.parse_args()

    pdf_dir = args.pdf_dir
    output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # import test according to argument
    reader = args.reader
    if reader == 'pymupdf':
        from pymupdf import test_extract_text
    elif reader == 'pdfminersix':
        from pdfminersix import test_extract_text
    elif reader == 'pypdf2':
        from pypdf2 import test_extract_text
    elif reader == 'pdfplumber':
        from pdfplumber import test_extract_text
    else:
        print('Reader not available for testing in this script')
    
    
    fname_list = []
    outcome_list = []
    time_start = time.perf_counter()

    # pdf_dir = Path('data/lcwa_gov_pdf_data/data')
    for pdf_file in os.listdir(pdf_dir):
        fname_list.append(pdf_file)
        fpath = (os.path.join(pdf_dir, pdf_file))
        outcome = test_extract_text(fpath)
        outcome_list.append(outcome)

    time_end = time.perf_counter()
    time_diff = f'{time_end - time_start:0.4f} seconds'


    output_reader_fpath = os.path.join(output_dir, reader + '.csv')
    with open(output_reader_fpath, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(fname_list, outcome_list))

    # append timing result 
    output_timing_fpath = os.path.join(output_dir, 'timing.csv')
    with open(output_timing_fpath, "a", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([reader, time_diff])



    