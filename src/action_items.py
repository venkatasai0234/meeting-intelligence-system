import json
from pathlib import Path
from typing import Dict, List


def save_action_items(action_items: List[Dict[str, str]], output_path: str) -> None:
    """
    Save extracted action items to a JSON file.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(action_items, file, indent=4)