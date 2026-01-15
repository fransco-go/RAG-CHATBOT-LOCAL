import os
from openai import OpenAI

class OpenRouterLLMService:
    def __init__(self, model: str = "google/gemma-3-27b-it:free"):
        # Pastikan Anda sudah menyimpan OPENROUTER_API_KEY di environment variables
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ.get("OPENROUTER_API_KEY"),
        )
        self.model = model

    def generate(self, question: str, context: list[str]) -> str:
        # Menggabungkan dokumen pendukung menjadi satu string konteks
        joined_context = "\n\n".join(context)

        prompt = f"""
        Anda adalah asisten yang membantu.
        Jawablah pertanyaan hanya berdasarkan konteks yang disediakan di bawah ini.

        Konteks:
        {joined_context}

        Pertanyaan:
        {question}

        Jawaban:
        """

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                extra_headers={
                    "HTTP-Referer": "http://localhost:8000", # Opsional untuk ranking OpenRouter
                    "X-Title": "ChatBot RAG Demo",
                }
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Terjadi kesalahan pada API OpenRouter: {str(e)}"