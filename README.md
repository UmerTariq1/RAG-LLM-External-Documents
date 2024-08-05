
# RAG-LLM-External-Documents

Welcome to the **RAG-LLM-External-Documents** repository! This project demonstrates the application of Retrieval-Augmented Generation (RAG) using a Language Learning Model (LLM) to create a sophisticated chatbot that can efficiently utilize external documents for answering user queries.

## Project Overview

This repository showcases the integration of RAG with a Llama3 GPT-style model to build a chatbot capable of providing detailed answers based on an external guide document. The primary goal is to demonstrate the powerful capabilities of LLMs when combined with RAG techniques.

### Key Steps in the Project:

1. **Preprocessing the Guide:**
   - The project begins by preprocessing a HackMD `.md` file. The [preprocess_hackmd.py](preprocess_hackmd.py) script converts the markdown file into a formatted `.txt` file with structured headings and body sections.

2. **Splitting the Text:**
   - Next, the [split_one_txt_to_multiple_hackmd.py](split_one_txt_to_multiple_hackmd.py) script splits the processed text file into smaller, manageable documents, making it easier for the model to handle.

3. **Creating the Chatbot:**
   - The core of this project is the `RAGChatbot` class found in the [rag_chatbot_psa.py](rag_chatbot_psa.py) file. This class leverages the Llama3 model to create a chatbot that can interact with users and provide responses based on the processed guide document.

## Usage

### Colab Notebook

A Colab notebook is provided for a comprehensive demonstration. This notebook guides you through:

1. **Deploying the Chatbot:**
   - Utilize the `RAGChatbot` class from the [rag_chatbot_psa.py](rag_chatbot_psa.py) file to create a chatbot.
   - Deploy the chatbot locally within the Colab environment using Streamlit for an interactive user interface.

You can access and run the Colab notebook [here](colab_notebook.ipynb).

### Streamlit Deployment

To deploy the chatbot using Streamlit locally:

1. Clone the repository:
   ```
   git clone https://github.com/UmerTariq1/RAG-LLM-External-Documents.git
   cd RAG-LLM-External-Documents
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Further Expansion

The framework provided in this repository can be expanded by incorporating additional documents or resources, enhancing the chatbot's capabilities. This project serves as a foundation for developing more complex RAG-based applications using LLMs.

## Acknowledgements

This project is inspired by the PSA guide to help new students in Germany and was created for educational purposes, primarily to demonstrate the practical application of RAG techniques with LLMs.

Feel free to explore, use, and enhance this repository. Contributions and suggestions are welcome!

For any questions or contributions, please open an issue or submit a pull request.

---

This repository is maintained by [Umer Tariq](https://github.com/UmerTariq1).

---

Enjoy using the RAG-LLM-External-Documents project!

---

### requirements.txt

```
datasets
sentence_transformers
faiss-gpu
faiss-cpu
accelerate
bitsandbytes
transformers
```

---

### Example Usage

To get started with this project, you can follow the provided Colab notebook or deploy the Streamlit app locally. Both methods showcase how to preprocess documents, split text files, and create a powerful chatbot using RAG and LLMs.

For a hands-on experience, refer to the [colab_notebook.ipynb](colab_notebook.ipynb).

---

This README provides a detailed overview of how to use RAG with LLMs to create a sophisticated chatbot. It highlights the preprocessing of documents, the creation of smaller text files, and the deployment of a Streamlit app for interactive use.
