from typing import Dict, Iterator, List
import typing

def filter_by_currency(transactions: List[Dict[str, any]], currency: str) -> Iterator[Dict[str, typing.Any]]:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:

            yield transaction


def transaction_descriptions(transactions: List[Dict[str, any]]) -> Iterator[str]:
    """Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for transaction in transactions:

        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Функция генератор, которая выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        # Форматируем номер карты, как строку с пробелами по 4 цифры
        card_number = f"{number:0>16}"

        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
