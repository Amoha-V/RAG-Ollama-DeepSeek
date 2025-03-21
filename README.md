**RAG-Ollama-DeepSeek** is a Retrieval-Augmented Generation (RAG) system powered by the **Ollama framework** and the **DeepSeek-R1 model**. It enables users to upload documents (e.g., PDFs), process them into chunks, and query the content using advanced NLP techniques. The system retrieves relevant document chunks and generates accurate, context-aware responses using the DeepSeek-R1 model. This project is ideal for research, document analysis, and intelligent question-answering applications.

---

### File Names and Descriptions:

1. **`requirements.txt`**  
   - Contains the list of Python dependencies required to run the project.  
   - Includes libraries like `streamlit`, `langchain`, `pdfplumber`, and `ollama`.

2. **`resumetemplate.pdf`**  
   - A sample PDF file used for testing the RAG system.  
   - Contains a resume template with sections like Education, Experience, Projects, and Technical Skills.

3. **`rag_deep.py`**  
   - The main Streamlit application script.  
   - Implements the RAG pipeline:  
     - Uploads and processes PDF documents.  
     - Splits text into chunks using `RecursiveCharacterTextSplitter`.  
     - Indexes chunks using Ollama embeddings and an in-memory vector store.  
     - Retrieves relevant chunks and generates answers using the DeepSeek-R1 model.

4. **`ollamatesting.py`**  
   - A simple script to test the Ollama framework with the DeepSeek-R1 model.  
   - Sends a query to the model and prints the response.

5. **`app.py`**  
   - A Streamlit-based chat application using the DeepSeek-R1 model.  
   - Allows users to interact with the AI assistant for general queries and coding-related questions.

---

### `README.md` File:

```markdown
# RAG-Ollama-DeepSeek

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-FF6F61?style=for-the-badge&logo=LangChain&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-00BFFF?style=for-the-badge&logo=Ollama&logoColor=white)

**RAG-Ollama-DeepSeek** is a Retrieval-Augmented Generation (RAG) system powered by the **Ollama framework** and the **DeepSeek-R1 model**. It allows users to upload documents, process them, and query the content using advanced NLP techniques. The system retrieves relevant document chunks and generates accurate, context-aware responses.

---

## Features

- **Document Upload**: Upload PDF documents for processing.
- **Text Chunking**: Split documents into smaller chunks for efficient retrieval.
- **Vector Embeddings**: Use Ollama embeddings to index document chunks.
- **Retrieval-Augmented Generation (RAG)**: Retrieve relevant chunks and generate answers using the DeepSeek-R1 model.
- **Interactive Chat**: Ask questions about the uploaded documents and get concise, factual answers.

---

## File Structure

```
RAG-Ollama-DeepSeek/
├── requirements.txt          # Python dependencies
├── resumetemplate.pdf        # Sample PDF for testing
├── rag_deep.py               # Main RAG application
├── ollamatesting.py          # Ollama + DeepSeek-R1 testing script
├── app.py                    # Streamlit chat application
└── README.md                 # Project documentation
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/RAG-Ollama-DeepSeek.git
   cd RAG-Ollama-DeepSeek
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Ollama is set up and the DeepSeek-R1 model is available.

---

## Usage

1. Run the RAG application:
   ```bash
   streamlit run rag_deep.py
   ```

2. Upload a PDF document and ask questions about its content.

3. For general chat, run the Streamlit chat app:
   ```bash
   streamlit run app.py
   ```

4. Test Ollama with the DeepSeek-R1 model:
   ```bash
   python ollamatesting.py
   ```

---

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **LangChain**: For document processing, text splitting, and RAG implementation.
- **Ollama**: For embeddings and interacting with the DeepSeek-R1 model.
- **PDFPlumber**: For extracting text from PDF documents.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Ollama](https://ollama.ai/) for providing the framework and DeepSeek-R1 model.
- [LangChain](https://www.langchain.com/) for the RAG pipeline and document processing tools.
- [Streamlit](https://streamlit.io/) for the interactive web app framework.
```

---

### Key Highlights:
- **Focus on RAG**: The repository emphasizes Retrieval-Augmented Generation, making it ideal for document-based question-answering systems.
- **Ollama + DeepSeek-R1**: The integration of Ollama and the DeepSeek-R1 model ensures high-quality embeddings and responses.
- **Streamlit UI**: Provides an interactive and user-friendly interface for document uploads and queries.
