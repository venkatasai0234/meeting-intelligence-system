from src.preprocess import load_transcript, clean_text, save_cleaned_transcript


def main() -> None:
    input_file = "data/raw/meeting1.txt"
    output_file = "data/processed/meeting1_cleaned.txt"

    transcript = load_transcript(input_file)
    cleaned_transcript = clean_text(transcript)
    save_cleaned_transcript(cleaned_transcript, output_file)

    print("Raw Transcript:\n")
    print(transcript)

    print("\n" + "=" * 50)
    print("Cleaned Transcript:\n")
    print(cleaned_transcript)

    print("\n" + "=" * 50)
    print(f"Cleaned transcript saved to: {output_file}")


if __name__ == "__main__":
    main()