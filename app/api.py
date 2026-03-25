from fastapi import FastAPI
from pydantic import BaseModel

from src.preprocess import (
    clean_text,
    split_transcript_lines,
    parse_transcript_lines,
    extract_action_items,
    extract_decisions,
)
from src.topics import segment_topics
from src.search import load_embedding_model, semantic_search
from src.output_formatter import build_meeting_output


app = FastAPI(title="Meeting Intelligence API", version="1.0.0")

model = load_embedding_model()


class MeetingRequest(BaseModel):
    transcript: str
    query: str = "What was decided about the demo?"


@app.get("/")
def root() -> dict:
    return {"message": "Meeting Intelligence API is running"}


@app.post("/analyze")
def analyze_meeting(request: MeetingRequest) -> dict:
    cleaned_transcript = clean_text(request.transcript)
    lines = split_transcript_lines(cleaned_transcript)
    records = parse_transcript_lines(lines)

    action_items = extract_action_items(records)
    decisions = extract_decisions(records)
    topics = segment_topics(records)
    search_results = semantic_search(request.query, records, model, top_k=3)

    output = build_meeting_output(
        action_items=action_items,
        decisions=decisions,
        topics=topics,
        search_results=search_results,
    )

    return output