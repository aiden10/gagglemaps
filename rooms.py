import pymupdf
import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
    path_to_poppler_exe = Path(r"C:\.....")
    out_directory = Path(r"~\Desktop").expanduser()
else:
    out_directory = Path("~").expanduser()  

def get_text(PDF_file):
    image_file_list = []
    with TemporaryDirectory() as tempdir:
        if platform.system() == "Windows":
            pdf_pages = convert_from_path(PDF_file, 500, poppler_path=path_to_poppler_exe)
        else:
            pdf_pages = convert_from_path(PDF_file, 500)
        
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")
            image_file_list.append(filename)
        
        for image_file in image_file_list:
            text = str(((pytesseract.image_to_string(Image.open(image_file)))))
            text = text.replace("-\n", "")
            print(text)
    
    with pymupdf.open(PDF_file) as doc:
        text = chr(12).join([page.get_text() for page in doc])
        print(text)

for file in os.listdir("floorPlans"):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        fn = os.path.join("floorPlans", filename)
        print(fn)
        get_text(fn)