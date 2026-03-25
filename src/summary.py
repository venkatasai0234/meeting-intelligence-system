from typing import Dict, List


def format_topic_overview(topic_names: List[str]) -> str:
    """
    Build a readable sentence from topic names.
    """
    if not topic_names:
        return "The meeting covered general discussion points."

    if len(topic_names) == 1:
        return f"The meeting focused on {topic_names[0]}."

    if len(topic_names) == 2:
        return f"The meeting focused on {topic_names[0]} and {topic_names[1]}."

    return (
        "The meeting focused on "
        + ", ".join(topic_names[:-1])
        + f", and {topic_names[-1]}."
    )


def generate_meeting_summary(
    action_items: List[Dict[str, str]],
    decisions: List[Dict[str, str]],
    topics: List[Dict[str, object]],
) -> Dict[str, object]:
    """
    Generate a simple structured meeting summary
    from extracted action items, decisions, and topics.
    """
    topic_names = [topic["topic"] for topic in topics if topic["topic"] != "general"]
    overview = format_topic_overview(topic_names)

    key_decisions = [item["text"] for item in decisions[:3]]
    key_action_items = [f"{item['speaker']}: {item['text']}" for item in action_items[:3]]

    return {
        "overview": overview,
        "key_decisions": key_decisions,
        "key_action_items": key_action_items,
    }