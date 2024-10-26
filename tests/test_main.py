import json
from unittest.mock import mock_open, patch

import pytest

from main.main import count_transactions_by_category, filter_transactions_by_description, load_transactions_from_json


def test_filter_transactions_by_description():
    transactions = [
        {"description": "Открытие вклада", "amount": 40542},
        {"description": "Перевод с карты на карту", "amount": 130},
        {"description": "Перевод организации", "amount": 8390},
    ]

    filtered = filter_transactions_by_description(transactions, "вклад")
    assert len(filtered) == 1
    assert filtered[0]["description"] == "Открытие вклада"

    filtered = filter_transactions_by_description(transactions, "перевод")
    assert len(filtered) == 2


def test_count_transactions_by_category():
    transactions = [
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]

    counts = count_transactions_by_category(transactions)
    assert counts["открытие вклада"] == 2
    assert counts["перевод с карты на карту"] == 1
    assert counts["перевод организации"] == 1


@patch("builtins.open", new_callable=mock_open, read_data='[{"description": "Тест", "amount": 100}]')
def test_load_transactions_from_json(mock_file):
    transactions = load_transactions_from_json("dummy_path.json")
    assert len(transactions) == 1
    assert transactions[0]["description"] == "Тест"
    assert transactions[0]["amount"] == 100


if __name__ == "__main__":
    pytest.main()
