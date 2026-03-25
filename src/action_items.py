from pathlib import Path
from typing import List


def save_action_items(action_items: List[str], output_path: str) -> None:
    """
    Save extracted action items to a text file.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        for idx, item in enumerate(action_items, start=1):
            file.write(f"{idx}. {item}\n")