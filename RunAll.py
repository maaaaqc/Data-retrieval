import ExcelConverter
import TextReader
import WordConverter

import os
import subprocess
import time
from pathlib import Path

FOLDER = Path.cwd() / "output"
EXCEL = Path.cwd() / "summary.xlsx"
WORD = Path.cwd() / "summary.docx"

def run_all():
    DICTIONARY = TextReader.extract_info(FOLDER)
    ExcelConverter.convert_excel(DICTIONARY, EXCEL)
    WordConverter.convert_word(DICTIONARY, WORD)
    

if __name__ == "__main__":
    run_all()