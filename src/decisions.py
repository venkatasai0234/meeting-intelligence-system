from pathlib import Path
from typing import List


def save_decisions(decisions: List[str], output_path: str) -> None:
    """
    Save extracted decisions to a text file.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        for idx, item in enumerate(decisions, start=1):
            file.write(f"{idx}. {item}\n")