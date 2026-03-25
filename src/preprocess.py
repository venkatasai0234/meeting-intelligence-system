import re
from pathlib import Path


def load_transcript(file_path: str) -> str:
    """
    Load a transcript from a text file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_text(text: str) -> str:
    """
    Basic transcript cleaning:
    - remove extra spaces
    - remove repeated newlines
    - strip leading/trailing whitespace
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def save_cleaned_transcript(text: str, output_path: str) -> None:
    """
    Save cleaned transcript text to a file.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)