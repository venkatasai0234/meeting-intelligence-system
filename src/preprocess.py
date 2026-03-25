import re
from pathlib import Path
from typing import Dict, List


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
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()


def save_cleaned_transcript(text: str, output_path: str) -> None:
    """
    Save cleaned transcript text to a file.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)


def split_transcript_lines(text: str) -> List[str]:
    """
    Split transcript into non-empty speaker lines.
    """
    lines = [line.strip() for line in text.split("\n")]
    return [line for line in lines if line]


def parse_speaker_line(line: str) -> Dict[str, str]:
    """
    Parse a transcript line into speaker and text.

    Example:
    'Sarah: I will send the revised deck tomorrow.'
    ->
    {'speaker': 'Sarah', 'text': 'I will send the revised deck tomorrow.'}
    """
    if ":" in line:
        speaker, text = line.split(":", 1)
        return {
            "speaker": speaker.strip(),
            "text": text.strip(),
        }

    return {
        "speaker": "Unknown",
        "text": line.strip(),
    }


def parse_transcript_lines(lines: List[str]) -> List[Dict[str, str]]:
    """
    Convert raw transcript lines into structured speaker-text records.
    """
    return [parse_speaker_line(line) for line in lines]


def extract_action_items(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Simple rule-based baseline for action item extraction.
    """
    action_patterns = [
        r"\bi will\b",
        r"\bwe should\b",
        r"\blet's\b",
        r"\blets\b",
        r"\bneed to\b",
        r"\bplan to\b",
        r"\bgoing to\b",
    ]

    action_items = []

    for record in records:
        lowered_text = record["text"].lower()
        if any(re.search(pattern, lowered_text) for pattern in action_patterns):
            action_items.append(record)

    return action_items


def extract_decisions(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Simple rule-based baseline for decision extraction.
    """
    decision_patterns = [
        r"\bdecided to\b",
        r"\bagreed to\b",
        r"\bwas finalized\b",
        r"\bfinalized that\b",
        r"\bconfirmed that\b",
        r"\bapproved\b",
    ]

    decisions = []

    for record in records:
        lowered_text = record["text"].lower()
        if any(re.search(pattern, lowered_text) for pattern in decision_patterns):
            decisions.append(record)

    return decisions