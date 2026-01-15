# 🤖 RAG Chatbot Service (FastAPI + Qdrant + OpenRouter)

Sistem Chatbot berbasis **Retrieval-Augmented Generation (RAG)** yang menggunakan FastAPI sebagai backend, Qdrant sebagai database vektor, dan OpenRouter sebagai penyedia model AI (Gemma 3).

## 🚀 Fitur Utama
- **Semantic Search**: Menggunakan Qdrant Vector Database.
- **Modern LLM**: Terintegrasi dengan Gemma 3 27B via OpenRouter.

## 📋 SET UP
- [Docker](https://www.docker.com/get-started).
- API Key dari [OpenRouter](https://openrouter.ai/).

## ⚙️ Persiapan
1. **Clone Repository**:
   ```bash
   git clone [https://github.com/username/rag-chatbot-project.git](https://github.com/username/rag-chatbot-project.git)
   cd rag-chatbot-project
   ```
2. **Masukkan OpenRouter API key pada file .env**:
    ```bash
    OPENROUTER_API_KEY=your_api_key_here
    QDRANT_HOST=qdrant
    QDRANT_PORT=6333
    ```

## 🐳 Menjalankan Aplikasi

Jalankan perintah berikut untuk membangun dan menyalakan semua layanan:

```bash
docker-compose up --build
```

Aplikasi dapat diakses local melalui:
1. API Backend: http://localhost:8000
2. Swagger UI (Docs): http://localhost:8000/docs
3. Qdrant Dashboard: http://localhost:6333/dashboard

