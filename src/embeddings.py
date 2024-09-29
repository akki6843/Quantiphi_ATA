"""
Code authored for Qunatiphi company. 
For the position of ATA.
Interview Round 2.
"""

from sentence_transformers import SentenceTransformer

from config import Config
from data_extraction import extract_text_from_pdf

def get_embeddings(data):
    model = SentenceTransformer(Config.EMBEDDING_MODEL)
    model.max_seq_length = Config.EMBEDDING_SIZE
    data_vectos = model.encode(data)
    return data_vectos


if __name__=="__main__":
    textbook_file = "./data/ConceptsofBiology-WEB.pdf"
    chaper_1, lines_1 = extract_text_from_pdf(textbook_file, 0, 20)
    embeddings_lines1 = get_embeddings(lines_1)
