# 🤖 RAG Chatbot Service (FastAPI + Qdrant + OpenRouter)

Sistem Chatbot berbasis **Retrieval-Augmented Generation (RAG)** yang menggunakan FastAPI sebagai backend, Qdrant sebagai database vektor, dan OpenRouter sebagai penyedia model AI (Gemma 3).

## 🚀 Fitur Utama
- **Semantic Search**: Menggunakan Qdrant `query_points` untuk pencarian konteks yang akurat.
- **Modern LLM**: Terintegrasi dengan Gemma 3 27B via OpenRouter.
- **Dockerized**: Seluruh layanan (App & DB) dapat dijalankan dengan satu perintah.
- **Persistence**: Data vektor tersimpan aman di volume lokal.

## 🛠️ Arsitektur Sistem
Sistem ini bekerja dengan alur:
1. **User Query** -> 2. **Embedding (OpenRouter)** -> 3. **Vector Search (Qdrant)** -> 4. **Augment Prompt** -> 5. **LLM Generation (Gemma 3)**.



## 📋 Prasyarat
- [Docker](https://www.docker.com/get-started) & Docker Compose installed.
- API Key dari [OpenRouter](https://openrouter.ai/).

## ⚙️ Persiapan
1. **Clone Repository**:
   ```bash
   git clone [https://github.com/username/rag-chatbot-project.git](https://github.com/username/rag-chatbot-project.git)
   cd rag-chatbot-project
   ```
2. **Masukkan OpenRouter API key pada file .env **:
    ```bash
    OPENROUTER_API_KEY=your_api_key_here
    QDRANT_HOST=qdrant
    QDRANT_PORT=6333
    ```

