import json
import os
from typing import List, Dict, Any


def load_transactions(filepath: str) -> List[Dict[str, Any]]:
    """Загружает финансовые транзакции из JSON-файла."""
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
        except (json.JSONDecodeError, TypeError):

            return []
