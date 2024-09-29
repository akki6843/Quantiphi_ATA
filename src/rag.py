"""
Code authored for Qunatiphi company. 
For the position of ATA.
Interview Round 2.
"""

from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline
import requests
from config import Config
from data_extraction import extract_text_from_pdf
from embeddings import get_embeddings


class RAG:
    def __init__(self, textbook_loc=Config.BOOK):
        self.model = SentenceTransformer(Config.EMBEDDING_MODEL)
        self.generator = pipeline('text-generation', model=Config.GENERATOR_MODEL)
        self.textbook_loc = textbook_loc
        self.get_data()  
        self.get_text()
        self.create_embedding()
        self.create_index()
    
    def get_data(self):
        response = requests.get(Config.BOOK_LINK)
        with open("sample.pdf", "wb") as file:
              file.write(response.content)
        print("PDF downloaded successfully!")

    def get_text(self, start_page = 5, end_page=130):
        _, self.lines_1 = extract_text_from_pdf(self.textbook_loc, start_page, end_page)
    
    def create_embedding(self):
        self.embeddings_lines1 = get_embeddings(self.lines_1)
    
    def create_index(self):
        self.index = faiss.IndexFlatL2(self.embeddings_lines1.shape[1])
        self.index.add(self.embeddings_lines1)
    
    
    def retrieve(self, query, k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k)
        return [self.lines_1[i] for i in indices[0]]

    def generate_answer(self,retrieved_chunks, question):
        context = " ".join(retrieved_chunks)
        input_text = f"Question: {question}\nContext: {context}\n Answer:"
        answer = self.generator(input_text, max_new_tokens=Config.MAX_NEW_TOKENS, num_return_sequences=1)
        return answer[0]['generated_text']


if __name__=="__main__":
    r = RAG()
    question = "what is explained in chapter 3?"
    retrieved_chunks = r.retrieve(question)
    answer = r.generate_answer(retrieved_chunks, question)
    print(answer)

    print("*************************************")
    question = "what is explained in chapter 1?"
    retrieved_chunks = r.retrieve(question)
    answer = r.generate_answer(retrieved_chunks, question)
    print(answer)