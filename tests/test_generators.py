import pytest
from src.generators.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions():
    return [
        {"operationAmount": {"currency": {"code": "USD", "value": 100}}, "description": "Transaction 1"},
        {"operationAmount": {"currency": {"code": "EUR", "value": 200}}, "description": "Transaction 2"},
        {"operationAmount": {"currency": {"code": "RUB", "value": 150}}, "description": "Transaction 3"}]

# Параметризованный тест для filter_by_currency
@pytest.mark.parametrize("currency, exit_count, exit_descriptions", [
    ("USD", 1, ["Transaction 1"]),
    ("EUR", 1, ["Transaction 2"]),
    ("GBP", 0, []),
    ("RUB", 1, ["Transaction 3"])])

def test_filter_by_currency(transactions, currency, exit_count, exit_descriptions):
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert len(filtered_transactions) == exit_count
    assert [t["description"] for t in filtered_transactions] == exit_descriptions


# Параметризованный тест для transaction_descriptions
@pytest.mark.parametrize("exit_descriptions", [
    ["Transaction 1", "Transaction 2", "Transaction 3"],])


def test_transaction_descriptions(transactions, exit_descriptions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == exit_descriptions


# Параметризованный тест для card_number_generator
@pytest.mark.parametrize("start, end, exit_card_numbers", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",]),
    (10, 12, [
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012",])])


def test_card_number_generator(start, end, exit_card_numbers):
    card_numbers = list(card_number_generator(start, end))
    assert card_numbers == exit_card_numbers