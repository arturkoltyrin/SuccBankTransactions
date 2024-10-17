import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv(".env")

API_KEY = os.getenv("API_KEY")  # Получение токена API


def convert_to_rub(transaction: dict) -> float:
    amount = transaction.get("Amount", 0.0)  # Получение суммы транзакции
    currency = transaction.get("Currency", "")  # Получение валюты транзакции

    if currency == "RUB":
        return float(amount)  # Если валюта в рублях, возвращаем сумму

    # Запрос к API для получения курса валют
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": currency, "to": "RUB", "amount": amount}

    headers = {"apikey": API_KEY}  # Использование токена API из переменных окружения

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json().get("result", 0.0)  # Возвращаем результат конвертации

    return 0.0  # Если произошла ошибка, возвращаем 0.0
