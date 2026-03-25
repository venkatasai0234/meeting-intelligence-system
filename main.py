from src.preprocess import (
    load_transcript,
    clean_text,
    save_cleaned_transcript,
    split_transcript_lines,
    parse_transcript_lines,
    extract_action_items,
    extract_decisions,
)
from src.topics import segment_topics
from src.search import load_embedding_model, semantic_search
from src.output_formatter import build_meeting_output, save_meeting_output


def main() -> None:
    input_file = "data/raw/meeting1.txt"
    cleaned_output_file = "data/processed/meeting1_cleaned.txt"
    final_output_file = "data/processed/meeting1_full_output.json"

    transcript = load_transcript(input_file)
    cleaned_transcript = clean_text(transcript)
    save_cleaned_transcript(cleaned_transcript, cleaned_output_file)

    lines = split_transcript_lines(transcript)
    records = parse_transcript_lines(lines)

    action_items = extract_action_items(records)
    decisions = extract_decisions(records)
    topics = segment_topics(records)

    model = load_embedding_model()
    query = "What was decided about the demo?"
    search_results = semantic_search(query, records, model, top_k=3)

    final_output = build_meeting_output(
        action_items=action_items,
        decisions=decisions,
        topics=topics,
        search_results=search_results,
    )

    save_meeting_output(final_output, final_output_file)

    print("\n" + "=" * 60)
    print("FINAL MEETING OUTPUT:\n")
    print(final_output)

    print("\n" + "=" * 60)
    print(f"Full output saved to: {final_output_file}")


if __name__ == "__main__":
    main()