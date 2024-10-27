from main.main import count_transactions_by_category, filter_transactions_by_description

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
    assert len(filtered) == 2  # Должно вернуть 2 транзакции

def test_count_transactions_by_category():
    transactions = [
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    categories = ["открытие вклада", "перевод с карты на карту", "перевод организации"]

    counts = count_transactions_by_category(transactions, categories)
    assert counts["открытие вклада"] == 2
    assert counts["перевод с карты на карту"] == 1
    assert counts["перевод организации"] == 1
