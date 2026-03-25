from typing import Dict, List

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model() -> SentenceTransformer:
    """
    Load the sentence transformer model.
    """
    return SentenceTransformer(MODEL_NAME)


def semantic_search(
    query: str,
    records: List[Dict[str, str]],
    model: SentenceTransformer,
    top_k: int = 3,
) -> List[Dict[str, object]]:
    """
    Perform semantic search over transcript records.

    Returns the top_k most relevant records with similarity scores.
    """
    if not records:
        return []

    texts = [record["text"] for record in records]

    query_embedding = model.encode([query])
    text_embeddings = model.encode(texts)

    similarity_scores = cosine_similarity(query_embedding, text_embeddings)[0]

    scored_results = []
    for record, score in zip(records, similarity_scores):
        scored_results.append({
            "speaker": record["speaker"],
            "text": record["text"],
            "score": float(score),
        })

    scored_results.sort(key=lambda item: item["score"], reverse=True)

    return scored_results[:top_k]