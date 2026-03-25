from src.preprocess import (
    clean_text,
    split_transcript_lines,
    parse_transcript_lines,
    extract_action_items,
    extract_decisions,
)


def test_clean_text() -> None:
    raw_text = "John: Hello   \n\nSarah: Hi"
    cleaned = clean_text(raw_text)

    assert cleaned == "John: Hello \nSarah: Hi"


def test_split_transcript_lines() -> None:
    text = "John: Hello\n\nSarah: Hi\n"
    lines = split_transcript_lines(text)

    assert lines == ["John: Hello", "Sarah: Hi"]


def test_parse_transcript_lines() -> None:
    lines = ["John: Hello", "Sarah: Hi"]
    records = parse_transcript_lines(lines)

    assert records == [
        {"speaker": "John", "text": "Hello"},
        {"speaker": "Sarah", "text": "Hi"},
    ]


def test_extract_action_items() -> None:
    records = [
        {"speaker": "John", "text": "We should send the proposal by Friday."},
        {"speaker": "Sarah", "text": "The pricing is still unclear."},
    ]

    action_items = extract_action_items(records)

    assert action_items == [
        {"speaker": "John", "text": "We should send the proposal by Friday."}
    ]


def test_extract_decisions() -> None:
    records = [
        {"speaker": "Mike", "text": "We decided to schedule a client review next Tuesday."},
        {"speaker": "Sarah", "text": "I will send the notes tomorrow."},
    ]

    decisions = extract_decisions(records)

    assert decisions == [
        {
            "speaker": "Mike",
            "text": "We decided to schedule a client review next Tuesday.",
        }
    ]