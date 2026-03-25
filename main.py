from src.preprocess import (
    load_transcript,
    clean_text,
    save_cleaned_transcript,
    split_transcript_lines,
    parse_transcript_lines,
    extract_action_items,
    extract_decisions,
)
from src.action_items import save_action_items
from src.decisions import save_decisions


def main() -> None:
    input_file = "data/raw/meeting1.txt"
    cleaned_output_file = "data/processed/meeting1_cleaned.txt"
    action_items_output_file = "data/processed/meeting1_action_items.json"
    decisions_output_file = "data/processed/meeting1_decisions.json"

    transcript = load_transcript(input_file)
    cleaned_transcript = clean_text(transcript)
    save_cleaned_transcript(cleaned_transcript, cleaned_output_file)

    lines = split_transcript_lines(transcript)
    records = parse_transcript_lines(lines)

    action_items = extract_action_items(records)
    decisions = extract_decisions(records)

    save_action_items(action_items, action_items_output_file)
    save_decisions(decisions, decisions_output_file)

    print("Structured Transcript Records:\n")
    for idx, record in enumerate(records, start=1):
        print(f"{idx}. Speaker: {record['speaker']}")
        print(f"   Text   : {record['text']}")

    print("\n" + "=" * 60)
    print("Detected Action Items:\n")
    if action_items:
        for idx, item in enumerate(action_items, start=1):
            print(f"{idx}. Speaker: {item['speaker']}")
            print(f"   Text   : {item['text']}")
    else:
        print("No action items found.")

    print("\n" + "=" * 60)
    print("Detected Decisions:\n")
    if decisions:
        for idx, item in enumerate(decisions, start=1):
            print(f"{idx}. Speaker: {item['speaker']}")
            print(f"   Text   : {item['text']}")
    else:
        print("No decisions found.")

    print("\n" + "=" * 60)
    print(f"Cleaned transcript saved to: {cleaned_output_file}")
    print(f"Action items saved to: {action_items_output_file}")
    print(f"Decisions saved to: {decisions_output_file}")


if __name__ == "__main__":
    main()