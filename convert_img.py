import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from concurrent.futures import ThreadPoolExecutor



def ocr_page(index_image_tuple):
    index, image = index_image_tuple
    text = pytesseract.image_to_string(image, lang='eng')
    return f"\n\n--- Page {index + 1} --\n{text}"

def convert_pdf_image_text(path: str, max_workers: int = 12) -> str:
    """
    Convert each page in a PDF into text using parallel OCR.
    """
    pages = convert_from_path(path, dpi=300)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(ocr_page, enumerate(pages)))

    return "".join(results)

if __name__ == "__main__":
    file_path = 'data/Alleged Communists in State Dept-EBF-62.pdf'
    extracted_text = convert_pdf_image_text(file_path, max_workers=8)

    with open("data/output_text.txt", 'w', encoding='utf-8') as f:
        f.write(extracted_text)

