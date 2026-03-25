import json
from pathlib import Path
from typing import Dict, List


TOPIC_KEYWORDS = {
    "proposal": ["proposal", "deck"],
    "client_review": ["client review", "client"],
    "pricing": ["pricing", "price"],
    "budget": ["budget"],
    "demo": ["demo"],
    "meeting_schedule": ["meeting", "schedule"],
}


def assign_topic(text: str) -> str:
    """
    Assign a topic label based on simple keyword matching.
    """
    lowered_text = text.lower()

    for topic, keywords in TOPIC_KEYWORDS.items():
        for keyword in keywords:
            if keyword in lowered_text:
                return topic

    return "general"


def segment_topics(records: List[Dict[str, str]]) -> List[Dict[str, object]]:
    """
    Group transcript records into topic buckets.
    """
    topic_map: Dict[str, List[Dict[str, str]]] = {}

    for record in records:
        topic = assign_topic(record["text"])

        if topic not in topic_map:
            topic_map[topic] = []

        topic_map[topic].append(record)

    segmented_topics = []
    for topic, items in topic_map.items():
        segmented_topics.append({
            "topic": topic,
            "items": items,
        })

    return segmented_topics


def save_topics(topics: List[Dict[str, object]], output_path: str) -> None:
    """
    Save topic segmentation output to a JSON file.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(topics, file, indent=4)