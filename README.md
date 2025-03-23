**RAG-Ollama-DeepSeek** is a Retrieval-Augmented Generation (RAG) system powered by the **Ollama framework** and the **DeepSeek-R1 model**. It enables users to upload documents (e.g., PDFs), process them into chunks, and query the content using advanced NLP techniques. The system retrieves relevant document chunks and generates accurate, context-aware responses using the DeepSeek-R1 model. This project is ideal for research, document analysis, and intelligent question-answering applications.

---

# RAG-Ollama-DeepSeek

<div align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/LangChain-00A300?style=for-the-badge&logo=LangChain&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Ollama-00BFFF?style=for-the-badge&logo=Ollama&logoColor=white" alt="Ollama"/>
  <img src="https://img.shields.io/badge/DeepSeek-6236FF?style=for-the-badge&logo=DeepSeek&logoColor=white" alt="DeepSeek"/>
</div>

## Overview

The system works by:
1. Extracting and processing text from uploaded documents
2. Splitting content into manageable chunks
3. Creating vector embeddings using Ollama
4. Retrieving the most relevant document sections based on user queries
5. Generating accurate, context-aware responses using the DeepSeek-R1 model

## Key Features

- **Document Processing**: Upload and process PDF documents with automatic text extraction
- **Intelligent Text Chunking**: Split documents into context-preserving chunks using RecursiveCharacterTextSplitter
- **Vector Embeddings**: Generate and store embeddings using Ollama's embedding capabilities
- **Semantic Search**: Find the most relevant document sections for any query
- **Context-Aware Responses**: Generate comprehensive answers by combining retrieved context with DeepSeek-R1's reasoning
- **Interactive UI**: Intuitive Streamlit interface for easy document upload and querying
- **Conversational Memory**: Maintain context across multiple questions about the same document

## Technology Stack

- **Streamlit**: Powers the interactive web interface
- **LangChain**: Orchestrates the document processing and RAG pipeline
- **Ollama**: Provides the framework for running the DeepSeek model locally
- **DeepSeek-R1**: Advanced language model for generating high-quality responses
- **PDFPlumber**: Extracts text from PDF documents

## Repository Structure

```
RAG-Ollama-DeepSeek/
├── requirements.txt        # Python dependencies
├── rag_deep.py             # Main RAG application with Streamlit UI
├── app.py                  # General-purpose DeepSeek chat application
├── ollamatesting.py        # Test script for Ollama + DeepSeek-R1
├── resumetemplate.pdf      # Sample PDF for testing
└── README.md               # Project documentation
```

## File Descriptions

### `requirements.txt`
- Contains the list of Python dependencies required to run the project
- Includes libraries like `streamlit`, `langchain`, `pdfplumber`, and `ollama`
- Essential for setting up the development environment correctly

### `resumetemplate.pdf`
- A sample PDF file used for testing the RAG system
- Contains a resume template with sections like Education, Experience, Projects, and Technical Skills
- Serves as example data for demonstration purposes

### `rag_deep.py`
- The main Streamlit application script that implements the complete RAG pipeline
- Functionality includes:
  - Uploading and processing PDF documents
  - Splitting text into chunks using `RecursiveCharacterTextSplitter`
  - Indexing chunks using Ollama embeddings and an in-memory vector store
  - Retrieving relevant chunks and generating answers using the DeepSeek-R1 model
  - Providing a user-friendly interface for document interaction

### `ollamatesting.py`
- A simple script to test the Ollama framework with the DeepSeek-R1 model
- Sends a query to the model and prints the response
- Useful for verifying that the Ollama installation and model are functioning correctly

### `app.py`
- A Streamlit-based chat application using the DeepSeek-R1 model
- Allows users to interact with the AI assistant for general queries and coding-related questions
- Provides a conversational interface without the document retrieval functionality

## `Demo Video`
  https://github.com/user-attachments/assets/536e33f5-62b0-4145-85c7-7c22bc068b10

## Installation

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running on your system
- DeepSeek-R1 model pulled in Ollama

### Step 1: Clone the repository

```bash
git clone https://github.com/Amoha-V/RAG-Ollama-DeepSeek.git
cd RAG-Ollama-DeepSeek
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set up Ollama with DeepSeek-R1

If you haven't already, pull the DeepSeek-R1 model using Ollama:

```bash
ollama pull deepseek:7b
```

## Usage

### Running the RAG Application

```bash
streamlit run rag_deep.py
```

This will start the main RAG application where you can:
1. Upload PDF documents
2. Ask questions about their content
3. Get AI-generated responses based on the document information

### Running the General Chat Application

```bash
streamlit run app.py
```

This launches a chat interface for general conversations with the DeepSeek-R1 model.

### Testing Ollama Integration

```bash
python ollamatesting.py
```

Use this script to test if Ollama and the DeepSeek-R1 model are properly configured.

## Example

1. Upload a resume PDF using the interface
2. Ask questions like:
   - "What are the technical skills mentioned in this resume?"
   - "Summarize the work experience in this document"
   - "What projects has this person worked on?"
3. The system will retrieve relevant sections and generate comprehensive answers

## Implementation Details

1. **Document Processing**:
   - PDFs are uploaded and text is extracted using PDFPlumber
   - Text is split into chunks using RecursiveCharacterTextSplitter with optimal parameters for preserving context

2. **Vector Storage**:
   - Document chunks are embedded using Ollama embeddings
   - Embeddings are stored in an in-memory vector store for quick retrieval

3. **Query Processing**:
   - User questions are embedded using the same embedding model
   - Most similar document chunks are retrieved based on semantic similarity

4. **Response Generation**:
   - Retrieved chunks are combined with the user query
   - DeepSeek-R1 model generates a comprehensive response using the context

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create your feature branch 
3. Commit your changes 
4. Push to the branch 
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Ollama for providing the framework to run models locally
- DeepSeek AI for their powerful language model
- LangChain for the RAG pipeline and document processing tools
- Streamlit for the interactive web app framework
