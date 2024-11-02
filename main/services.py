import json
import re
import logging
from typing import List, Dict
from src.utils.load_json import load_transactions

# Настройка логирования
logger = logging.getLogger("main.services")
logger.setLevel(logging.DEBUG)


def find_personal_transfers(transactions: List[Dict], name: str) -> List[Dict]:
    """Находит переводы, относящиеся к физическим лицам."""
    name_regex = rf"{name} [А-Я]\."

    transfers = [
        trans for trans in transactions
        if trans['category'] == "Переводы" and re.search(name_regex, trans['description'])]

    logger.debug(f"Найдено {len(transfers)} переводов для {name}.")
    return transfers


def get_currency_rates() -> List[Dict]:
    """Получает курс валют (пример)."""
    return [{'currency': 'USD', 'rate': 73.21}, {'currency': 'EUR', 'rate': 87.08}]


def get_stock_prices() -> List[Dict]:
    """Получает цены акций S&P500 (пример)."""
    return [
        {"stock": "AAPL", "price": 150.12},
        {"stock": "AMZN", "price": 3173.18},
        {"stock": "GOOGL", "price": 2742.39},
        {"stock": "MSFT", "price": 296.71},
        {"stock": "TSLA", "price": 1007.08}]
