"""
Code authored for Qunatiphi company. 
For the position of ATA.
Interview Round 2.
"""
import PyPDF2


def extract_text_from_pdf(pdf_path, start_page, end_page):
    """
    Function to extract data from target pages of PDF.
    """
    text = ""
    lines = []
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(start_page, end_page):
            page = reader.pages[page_num]
            text += page.extract_text()
            lines.extend(page.extract_text().splitlines())
    return text, lines

def clean_text(text):
    "Dummy Function that can be used to perform data cleaning."
    return text


if __name__=="__main__":
    print("Executing data extraction")
    textbook_file = "./data/ConceptsofBiology-WEB.pdf"
    chaper_1, lines_1 = extract_text_from_pdf(textbook_file, 5, 130)
    lines_1 = list(map(clean_text, lines_1))
