import pandas as pd
from typing import List, Dict


def load_transactions_from_csv(filepath: str) -> List[Dict[str, str]]:
    """Считывает финансовые операции из файла CSV."""
    try:
        data = pd.read_csv(filepath)
        return data.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"Ошибка при считывании файла CSV: {e}")


def load_transactions_from_excel(filepath: str) -> List[Dict[str, str]]:
    """Считывает финансовые операции из файла Excel."""
    try:
        data = pd.read_excel(filepath)
        return data.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"Ошибка при считывании файла Excel: {e}")
