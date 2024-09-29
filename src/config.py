"""
Code authored for Qunatiphi company. 
For the position of ATA.
Interview Round 2.
"""

class Config:
    EMBEDDING_MODEL = "ashakthy/biology"
    GENERATOR_MODEL = "ashakthy/biology"
    EMBEDDING_SIZE = 768
    MAX_NEW_TOKENS = 300
    BOOK_LINK = "https://assets.openstax.org/oscms-prodcms/media/documents/ConceptsofBiology-WEB.pdf?_gl=1*s5knas*_gcl_au*MTQxNTA5MzAxMS4xNzI3MzYzOTQ1*_ga*NjQ4ODA0NDk0LjE3MjczNjM5NDU.*_ga_T746F8B0QC*MTcyNzYzNjE1Mi4yLjEuMTcyNzYzNjE1Mi42MC4wLjA."
    BOOK = "./sample.pdf"