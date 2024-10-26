import json
import re
from collections import defaultdict
from typing import Dict, List, Union


def filter_transactions_by_description(
    transactions: List[Dict[str, Union[str, float]]], search_string: str
) -> List[Dict[str, Union[str, float]]]:
    """Фильтрует список транзакций по описанию с использованием регулярных выражений."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Регулярное выражение для поиска
    filtered_transactions = [trans for trans in transactions if pattern.search(trans.get("description", ""))]

    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict[str, str]]) -> Dict[str, int]:
    """Подсчитывает количество операций в каждой категории."""
    count_dict = defaultdict(int)

    for transaction in transactions:
        category = transaction.get("description", "").lower()  # Приводим к нижнему регистру для унификации
        count_dict[category] += 1

    return dict(count_dict)


def load_transactions_from_json(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """Загружает транзакции из JSON-файла."""
    with open(file_path, "r", encoding="utf-8") as f:

        return json.load(f)


def main() -> None:
    """Основная функция, которая отвечает за логику работы программы.
    Обработает пользовательский ввод и взаимодействие с банковскими транзакциями."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        transactions = load_transactions_from_json("transactions.json")  # Замените на ваш файл
        print("Для обработки выбран JSON-файл.")

        valid_statuses = {"executed", "canceled", "pending"}

        while True:
            status = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
            ).lower()
            if status in valid_statuses:
                print(f'Операции отфильтрованы по статусу "{status.upper()}"')
                break
            else:
                print(f'Статус операции "{status}" недоступен.')

        # Фильтрация по статусу
        filtered_transactions = [trans for trans in transactions if trans["status"].lower() == status]

        # Сортировка
        sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").lower()
        if sort_choice == "да":
            order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
            if order == "по возрастанию":
                filtered_transactions.sort(key=lambda x: x["date"])
            elif order == "по убыванию":
                filtered_transactions.sort(key=lambda x: x["date"], reverse=True)

        # Фильтрация по валюте
        currency_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower() == "да"
        if currency_choice:
            filtered_transactions = [trans for trans in filtered_transactions if trans["currency"] == "RUB"]

        # Фильтрация по описанию
        description_filter = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
        ).lower()
        if description_filter == "да":
            search_string = input("Введите строку для поиска в описании: ")
            filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

        # Вывод результата
        if filtered_transactions:
            print("Распечатываю итоговый список транзакций...")
            for trans in filtered_transactions:
                print(
                    f"\n{trans['date']} {trans['description']}\nСчет {trans['account']}\nСумма: {trans['amount']} {trans['currency']}\n"
                )
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
