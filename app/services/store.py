from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import uuid
import os

class DocumentStore:
    """
    Handles document storage and retrieval.
    Uses Qdrant if available, otherwise falls back to in-memory storage.
    """
    def __init__(self, embedding_service):
        self.embedding = embedding_service
        self.docs_memory = []
        self.using_qdrant = False
        self._init_qdrant()

    def _init_qdrant(self):
        try:
            qdrant_host = os.environ.get("QDRANT_HOST", "localhost")
            qdrant_port = int(os.environ.get("QDRANT_PORT", 8333)) 
            self.qdrant = QdrantClient(host=qdrant_host, port=qdrant_port)
            
            # self.qdrant = QdrantClient("http://localhost:8333")
            
            collections = self.qdrant.get_collections().collections
            exists = any(c.name == "demo_collection" for c in collections)
            
            if not exists:
                self.qdrant.create_collection(
                    collection_name="demo_collection",
                    vectors_config=VectorParams(size=self.embedding.dim, distance=Distance.COSINE)
                )
            self.using_qdrant = True
        except Exception:
            self.using_qdrant = False

    def add(self, text: str) -> int:
        emb = self.embedding.embed(text)
        doc_id = str(uuid.uuid4()) # Membuat ID unik berupa string
        payload = {"text": text}

        if self.using_qdrant:
            self.qdrant.upsert(
                collection_name="demo_collection",
                points=[PointStruct(id=doc_id, vector=emb, payload=payload)]
            )
        else:
            self.docs_memory.append(text)

        return doc_id

    def search(self, query: str, limit: int = 2) -> list[str]:
        # 1. Dapatkan vektor dari OpenRouter
        emb = self.embedding.embed(query)
        results = []

        if self.using_qdrant and self.qdrant:
            try:
                # 2. Used query_points 
                response = self.qdrant.query_points(
                    collection_name="demo_collection",
                    query=emb, # Mengirimkan list[float] hasil embedding
                    limit=limit,
                    with_payload=True # Memastikan payload ikut diambil
                )
                # 3. Ambil data teks dari hasil points
                results = [hit.payload["text"] for hit in response.points]
            except Exception as e:
                print(f"Pencarian QueryPoints gagal: {e}")
                self.using_qdrant = False 
        
        # Logika in-memory fallback (tetap sama)
        if not results:
            for doc in self.docs_memory:
                if query.lower() in doc.lower():
                    results.append(doc)
        
        return results

    def status(self):
        return {
            "qdrant_ready": self.using_qdrant,
            "in_memory_docs_count": len(self.docs_memory)
        }