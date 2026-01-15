import os
from openai import OpenAI

class OpenRouterEmbeddingService:
    def __init__(self, model: str = "google/gemini-embedding-001"):
        # Menggunakan client yang sama dengan LLM
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ.get("OPENROUTER_API_KEY"),
        )
        self.model = model
        # Dimensi google/gemini-embedding-001 adalah 768
        self.dim = 768 

    def embed(self, text: str) -> list[float]:
            try:
                response = self.client.embeddings.create(
                    model=self.model,
                    input=text,
                    encoding_format="float"
                )
                return response.data[0].embedding
            except Exception as e:
                print(f"Error pada Embedding OpenRouter: {e}")
                # Kembalikan vektor nol jika terjadi error agar aplikasi tidak crash
                return [0.0] * self.dim