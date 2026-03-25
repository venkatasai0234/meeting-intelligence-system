from src.preprocess import (
    load_transcript,
    clean_text,
    save_cleaned_transcript,
    split_transcript_lines,
    extract_action_items,
)
from src.action_items import save_action_items


def main() -> None:
    input_file = "data/raw/meeting1.txt"
    cleaned_output_file = "data/processed/meeting1_cleaned.txt"
    action_items_output_file = "data/processed/meeting1_action_items.txt"

    transcript = load_transcript(input_file)
    cleaned_transcript = clean_text(transcript)
    save_cleaned_transcript(cleaned_transcript, cleaned_output_file)

    lines = split_transcript_lines(transcript)
    action_items = extract_action_items(lines)
    save_action_items(action_items, action_items_output_file)

    print("Raw Transcript:\n")
    print(transcript)

    print("\n" + "=" * 60)
    print("Detected Action Items:\n")

    if action_items:
        for idx, item in enumerate(action_items, start=1):
            print(f"{idx}. {item}")
    else:
        print("No action items found.")

    print("\n" + "=" * 60)
    print(f"Cleaned transcript saved to: {cleaned_output_file}")
    print(f"Action items saved to: {action_items_output_file}")


if __name__ == "__main__":
    main()