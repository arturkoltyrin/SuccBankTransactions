import json
import pandas as pd
from datetime import datetime
from services import get_currency_rates, get_stock_prices
from reports import spending_by_weekday
from src.utils.load_json import load_transactions
from src.masks import get_mask_account

def greeting_based_on_time(datetime_str: str) -> str:
    """Возвращает приветствие в зависимости от времени суток."""
    hour = pd.to_datetime(datetime_str).hour
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def calculate_card_totals(transactions) -> list:
    """Рассчитывает общую сумму расходов и кешбэк по картам."""

    card_totals = []
    grouped = {}

    for transaction in transactions:
        card_number = transaction.get('card', '')
        masked_card_number = get_mask_account(card_number)
        amount = transaction.get('operationAmount', {}).get('amount', 0)
        if masked_card_number not in grouped:
            grouped[masked_card_number] = 0

        grouped[masked_card_number] += amount

    for card, total_spent in grouped.items():
        cashback = total_spent / 100  # Кешбэк 1 рубль на 100 рублей
        card_totals.append({
            'masked_card': card,
            'total_spent': total_spent,
            'cashback': cashback})

    return card_totals


def main(datetime_str: str) -> dict:
    """Основная функция для получения информации о переводах и отчетов."""
    greeting = greeting_based_on_time(datetime_str)

    # Загрузка транзакций из JSON файла
    transactions = load_transactions("C:/Users/user/PycharmProjects/SuccBankTransactions/data/operations.json")

    # Получение данных о картах
    card_totals = calculate_card_totals(transactions)

    # 5 транзакций по сумме платежа
    top_transactions = sorted(transactions, key=lambda x: x['operationAmount']['amount'], reverse=True)[:5]

    # Получение курсов валют и цен акций
    currency_rates = get_currency_rates()
    stock_prices = get_stock_prices()

    response = {
        "greeting": greeting,
        "cards": card_totals,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices}

    return response


