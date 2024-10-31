import re
import pandas as pd
from collections import Counter
from typing import List, Dict, Union
from src.decorators.decorators import log
from src.external_api.external_api import convert_to_rub
from src.generators.generators import filter_by_currency
from src.processing.processing import filter_by_state, sort_by_date
from src.reading_financial_transactions_from_CSV_XLSX_files.read_financ_transactions import load_transactions_from_csv, \
    load_transactions_from_excel
from src.utils.load_json import load_transactions
from src.widget.mask_account_card import mask_account_card, get_date


@log()
def filter_transactions_by_description(
        transactions: List[Dict[str, Union[str, float]]], search_string: str
) -> List[Dict[str, Union[str, float]]]:
    """Фильтрует список транзакций по описанию с использованием регулярных выражений."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [trans for trans in transactions if pattern.search(trans.get('description', ''))]


@log()
def count_transactions_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций в каждой категории."""
    count_dict = Counter()
    for transaction in transactions:
        category = transaction.get('description', '').lower()
        if category in categories:
            count_dict[category] += 1
    return dict(count_dict)


@log()
def main() -> None:
    """Основная функция, которая отвечает за логику работы программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    # Загрузка данных в зависимости от выбора пользователя
    if choice == '1':
        file_name = input("Введите имя JSON файла: ").strip()
        transactions = load_transactions(file_name)
    elif choice == '2':
        file_name = input("Введите имя CSV файла: ").strip()
        transactions = load_transactions_from_csv(file_name)
    elif choice == '3':
        file_name = input("Введите имя XLSX файла: ").strip()
        transactions = load_transactions_from_excel(file_name)
    else:
        print("Не поддерживаемый формат. Программа завершает работу.")
        return

    print("Файл успешно загружен.")
    print(transactions)
    # Фильтрация по статусу
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()
        if status in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            filtered_transactions = filter_by_state(transactions, status)
            print(filtered_transactions)
            break
        else:
            print(f'Статус операции "{status}" недоступен.')
    print(filtered_transactions)
    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_choice == 'да':
        order = input(
            "Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ").strip().lower()
        if order == 'по убыванию':
            filtered_transactions = sort_by_date(filtered_transactions, reverse=True)  # Передаем reverse=True
        else:
            filtered_transactions = sort_by_date(filtered_transactions)  # По умолчанию reverse=False
    print(filtered_transactions)
    # Фильтрация по рублевым транзакциям
    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ")
    if currency_choice.lower() == "да":
        filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
    print(filtered_transactions)
    # Фильтрация по описанию
    description_filter = input("Отфильтровать список транзакций по слову в описании? (Да/Нет): ").strip().lower()
    if description_filter == 'да':
        search_string = input("Введите строку для поиска в описании: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)
    print(filtered_transactions)
    # Вывод итогового списка транзакций
    if filtered_transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for trans in filtered_transactions:
            try:
                masked_from = mask_account_card(trans.get("from", ""))
            except ValueError:
                masked_from = "Не указан"

            try:
                masked_to = mask_account_card(trans.get("to", ""))
            except ValueError:
                masked_to = "Не указан"

            print(f"""{get_date(trans['date'])} {trans['description']}\n
            {masked_from} ➜ {masked_to}
            Сумма: {trans["operationAmount"]['amount']} {trans["operationAmount"]["currency"]["code"]}
        """)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == '__main__':
    main()
