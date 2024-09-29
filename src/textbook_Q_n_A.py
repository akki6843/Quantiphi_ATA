"""
Code authored for Qunatiphi company. 
For the position of ATA.
Interview Round 2.
"""

import streamlit as st

from rag import RAG

def execute():
    st.title("Textbook Q&A")
    rag_object = RAG()
    question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        retrieved_chunks = rag_object.retrieve(question)
        answer = rag_object.generate_answer(retrieved_chunks, question)
        st.write(answer)

if __name__=="__main__":
    execute()