from fastapi import FastAPI, UploadFile, File, HTTPException
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
from src.summary import generate_meeting_summary


app = FastAPI(title="Meeting Intelligence API", version="1.0.0")

model = load_embedding_model()


class MeetingRequest(BaseModel):
    transcript: str
    query: str = "What was decided about the demo?"


def run_pipeline(transcript: str, query: str) -> dict:
    cleaned_transcript = clean_text(transcript)
    lines = split_transcript_lines(cleaned_transcript)
    records = parse_transcript_lines(lines)

    action_items = extract_action_items(records)
    decisions = extract_decisions(records)
    topics = segment_topics(records)
    search_results = semantic_search(query, records, model, top_k=3)
    summary = generate_meeting_summary(
        action_items=action_items,
        decisions=decisions,
        topics=topics,
    )

    output = build_meeting_output(
        summary=summary,
        action_items=action_items,
        decisions=decisions,
        topics=topics,
        search_results=search_results,
    )

    return output


@app.get("/")
def root() -> dict:
    return {"message": "Meeting Intelligence API is running"}


@app.post("/analyze")
def analyze_meeting(request: MeetingRequest) -> dict:
    return run_pipeline(request.transcript, request.query)


@app.post("/analyze-file")
async def analyze_meeting_file(
    file: UploadFile = File(...),
    query: str = "What was decided about the demo?",
) -> dict:
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are supported.")

    content = await file.read()
    transcript = content.decode("utf-8")

    return run_pipeline(transcript, query)