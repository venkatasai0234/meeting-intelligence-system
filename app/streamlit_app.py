import sys
import os
from io import StringIO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

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


st.set_page_config(page_title="Meeting Intelligence System", layout="wide")

st.title("Meeting Intelligence System")
st.write("Upload a meeting transcript and analyze action items, decisions, topics, and semantic search results.")

model = load_embedding_model()


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

    return build_meeting_output(
        summary=summary,
        action_items=action_items,
        decisions=decisions,
        topics=topics,
        search_results=search_results,
    )


uploaded_file = st.file_uploader("Upload transcript (.txt)", type=["txt"])
query = st.text_input("Ask a question about the meeting", value="What was decided about the demo?")

if uploaded_file is not None:
    transcript = StringIO(uploaded_file.getvalue().decode("utf-8")).read()

    st.subheader("Transcript Preview")
    st.text_area("Transcript Content", transcript, height=200)

    if st.button("Analyze Meeting"):
        with st.spinner("Analyzing meeting..."):
            output = run_pipeline(transcript, query)

        st.success("Analysis complete")

        st.subheader("Summary")
        st.json(output["summary"])

        st.subheader("Action Items")
        if output["action_items"]:
            st.json(output["action_items"])
        else:
            st.write("No action items found.")

        st.subheader("Decisions")
        if output["decisions"]:
            st.json(output["decisions"])
        else:
            st.write("No decisions found.")

        st.subheader("Topics")
        if output["topics"]:
            st.json(output["topics"])
        else:
            st.write("No topics found.")

        st.subheader("Search Results")
        if output["search_results"]:
            st.json(output["search_results"])
        else:
            st.write("No search results found.")

        st.subheader("Full Output JSON")
        st.json(output)