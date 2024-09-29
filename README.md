# Custom RAG Implementation

This repository contains the implementation of a Custom Retrieval-Augmented Generation (RAG) model.

## Folder Structure

Repo/  
├── src/  
│   ├── data/  
│   ├── __init__.py  
│   ├── textbook_rag.py  
│   └── utils.py   
├── Docs/  
│   ├── architecture.md  
│   └── evaluation_results.md  
├── Notebooks/  
│   └── backend_evaluation.ipynb  
├── Dockerfile  
├── quantiphi.yaml  
└── README.md  


## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.8+
- Streamlit
- Docker (if you plan to containerize the application)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/akki6843/Quantiphi_ATA.git
    cd Quantiphi_ATA
    ```

2. Install miniconda from internet.  


3. Install the required dependencies:
    ```sh
    conda env create -f quantiphi.yaml
    ```

## Usage

### Running the Code

1. **Without Streamlit:**

    Navigate to the `src` folder and execute the following command:
    ```sh
    python rag.py
    ```

2. **With Streamlit:**

    To run the Streamlit version, execute the following command from the root directory:
    ```sh
    python -m streamlit run .\src\textbook_Q_n_A.py
    ```

### Notebooks

The `Notebooks` folder contains a Jupyter Notebook with the complete logic for the RAG implementation. You can open and run this notebook to understand the implementation details and experiment with the model.

### Documentation

The `Docs` folder contains detailed design documents. Refer to these documents for a comprehensive understanding of the system architecture and design choices.

### Docker

To build and run the Docker container, use the provided `Dockerfile`:
```sh
docker build -t custom-rag .
docker run -p 8501:8501 custom-rag
