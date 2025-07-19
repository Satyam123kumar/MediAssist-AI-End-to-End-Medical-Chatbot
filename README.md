# MediAssist-AI: End-to-End Medical Chatbot

An intelligent medical chatbot designed to provide accurate, fact-grounded answers from a trusted medical encyclopedia. This project uses a Retrieval-Augmented Generation (RAG) architecture to ensure reliability and minimize misinformation.

## ✨ Features

* **Fact-Grounded Responses:** Leverages a RAG pipeline to retrieve relevant information from a medical knowledge base before generating an answer.
* **Real-Time Conversational Interface:** A clean and responsive web interface for seamless user interaction.
* **Conversational Memory:** Remembers the context of the conversation for coherent follow-up questions.
* **Modern AI Stack:** Powered by Google's Gemini Pro for advanced reasoning and Pinecone for efficient, scalable vector search.
* **Easy to Run:** Fully containerized with clear setup instructions.

## ⚙️ How It Works

The application follows a Retrieval-Augmented Generation (RAG) workflow to ensure that the answers are based on factual data from the medical encyclopedia.

1.  **User Query:** The user asks a question through the Flask web interface.
2.  **Embedding:** The query is transformed into a vector embedding using a Hugging Face model.
3.  **Vector Search:** Pinecone searches the vector database to find the most relevant document chunks from the medical encyclopedia.
4.  **Augmentation:** The retrieved text chunks are combined with the original query to form an augmented prompt.
5.  **Generation:** The augmented prompt is sent to the Gemini Pro LLM, which generates a final, context-aware answer.
6.  **Chat History:** The conversation is stored in memory to handle follow-up questions effectively.

## 🛠️ Tech Stack

* **Language:** Python
* **Backend:** Flask
* **LLM Framework:** LangChain
* **LLM:** Google Gemini
* **Vector Database:** Pinecone
* **Embedding Model:** Hugging Face `sentence-transformers`
* **Frontend:** HTML, CSS, JavaScript

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* Git
* Python 3.8 or higher

### Installation & Setup

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/Satyam123kumar/MediAssist-AI-End-to-End-Medical-Chatbot.git](https://github.com/Satyam123kumar/MediAssist-AI-End-to-End-Medical-Chatbot.git)
    cd MediAssist-AI-End-to-End-Medical-Chatbot
    ```

2.  **Create a Virtual Environment**
    ```sh
    python -m venv medibot
    ```
    Activate the environment:
    * On Windows:
        ```sh
        medibot\scripts\activate
        ```
    * On macOS/Linux:
        ```sh
        source medibot/bin/activate
        ```

3.  **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    Create a `.env` file in the root directory of the project and add your API keys:
    ```env
    PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    ```

5.  **Store Embeddings in Pinecone**
    Run the following script once to process your data and store the embeddings in your Pinecone index.
    ```sh
    python store_index.py
    ```

6.  **Run the Application**
    ```sh
    python app.py
    ```

7.  **Open the Chatbot**
    Navigate to `http://127.0.0.1:8080` in your web browser.

## License

Distributed under the MIT License. See `LICENSE` for more information.
