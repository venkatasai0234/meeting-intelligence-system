from typing import Dict, List

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model() -> SentenceTransformer:
    """
    Load the sentence transformer model.
    """
    return SentenceTransformer(MODEL_NAME)


def detect_query_intent(query: str) -> str:
    """
    Detect the likely intent of the query.
    """
    lowered_query = query.lower()

    decision_keywords = ["decide", "decided", "decision", "agreed", "finalized", "approved"]
    action_keywords = ["action", "task", "owner", "who will", "who is", "follow up", "send", "schedule"]

    if any(keyword in lowered_query for keyword in decision_keywords):
        return "decision"

    if any(keyword in lowered_query for keyword in action_keywords):
        return "action"

    return "general"


def semantic_search(
    query: str,
    records: List[Dict[str, str]],
    model: SentenceTransformer,
    top_k: int = 3,
) -> List[Dict[str, object]]:
    """
    Perform semantic search over transcript records.

    Returns the top_k most relevant records with similarity scores.
    Applies a simple intent-aware score boost.
    """
    if not records:
        return []

    texts = [record["text"] for record in records]

    query_embedding = model.encode([query])
    text_embeddings = model.encode(texts)

    similarity_scores = cosine_similarity(query_embedding, text_embeddings)[0]
    query_intent = detect_query_intent(query)

    scored_results = []
    for record, score in zip(records, similarity_scores):
        boosted_score = float(score)
        lowered_text = record["text"].lower()

        if query_intent == "decision":
            decision_patterns = ["decided", "agreed", "finalized", "approved", "confirmed"]
            if any(pattern in lowered_text for pattern in decision_patterns):
                boosted_score += 0.15

        elif query_intent == "action":
            action_patterns = ["i will", "we should", "let's", "lets", "need to", "plan to", "going to"]
            if any(pattern in lowered_text for pattern in action_patterns):
                boosted_score += 0.15

        scored_results.append({
            "speaker": record["speaker"],
            "text": record["text"],
            "score": boosted_score,
        })

    scored_results.sort(key=lambda item: item["score"], reverse=True)

    return scored_results[:top_k]