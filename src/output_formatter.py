import json
from pathlib import Path
from typing import Dict, List


def build_meeting_output(
    summary: Dict,
    action_items: List[Dict],
    decisions: List[Dict],
    topics: List[Dict],
    search_results: List[Dict],
) -> Dict:
    """
    Combine extracted meeting intelligence into one structured dictionary.
    """
    return {
        "summary": summary,
        "action_items": action_items,
        "decisions": decisions,
        "topics": topics,
        "search_results": search_results,
    }


def save_meeting_output(output: Dict, output_path: str) -> None:
    """
    Save final meeting intelligence output to a JSON file.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4)