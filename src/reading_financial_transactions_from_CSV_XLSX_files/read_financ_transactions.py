from typing import Dict, List

import pandas as pd


def load_transactions_from_csv(filepath: str) -> List[Dict[str, str]]:
    """Считывает финансовые операции из файла CSV."""
    try:
        data = pd.read_csv(filepath)
        transactions = data.to_dict(orient="records")
        return [{'id': str(t['id']),
                 'state': t['state'],
                 'date': t['date'],
                 'amount': str(t['amount']),
                 'currency_name': t['currency_name'],
                 'currency_code': t['currency_code'],
                 'from': t['from'],
                 'to': t['to'],
                 'description': t['description']} for t in transactions]
    except Exception as e:
        raise Exception(f"Ошибка при считывании файла CSV: {e}")


def load_transactions_from_excel(filepath: str) -> List[Dict[str, str]]:
    """Считывает финансовые операции из файла Excel."""
    try:
        data = pd.read_excel(filepath)
        transactions = data.to_dict(orient="records")
        return [{'id': str(t['id']),
                 'state': t['state'],
                 'date': t['date'],
                 'amount': str(t['amount']),
                 'currency_name': t['currency_name'],
                 'currency_code': t['currency_code'],
                 'from': t['from'],
                 'to': t['to'],
                 'description': t['description']} for t in transactions]
    except Exception as e:
        raise Exception(f"Ошибка при считывании файла Excel: {e}")
