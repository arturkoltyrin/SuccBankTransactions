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
from src.masks import get_mask_card_number, get_mask_account


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
    count_dict = dict.fromkeys(categories, 0)
    for transaction in transactions:
        category = transaction.get('description', '').lower()
        if category in count_dict:
            count_dict[category] += 1
    return count_dict


@log()
def count_transactions_by_type(transactions: List[Dict[str, str]], transaction_type: str) -> int:
    """Подсчитывает количество операций определенного типа."""
    return Counter(trans['description'] for trans in transactions)[transaction_type]


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

    # Фильтрация по статусу
    valid_statuses = {"executed", "canceled", "pending"}
    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").lower()
        if status in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            filtered_transactions = filter_by_state(transactions, status)
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    # Конвертация валюты
    convert_currency = input("Конвертировать суммы в рубли? (Да/Нет): ").strip().lower()
    if convert_currency == 'да':
        for trans in filtered_transactions:
            trans['amount'] = convert_to_rub(trans)

    # Фильтрация по описанию
    description_filter = input("Отфильтровать список транзакций по слову в описании? (Да/Нет): ").strip().lower()
    if description_filter == 'да':
        search_string = input("Введите строку для поиска в описании: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_choice == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ").strip().lower()
        if order == 'по убыванию':
            filtered_transactions = sort_by_date(filtered_transactions, reverse=True)

    # Вывод итогового списка транзакций
    if filtered_transactions:
        print("Распечатываю итоговый список транзакций...")
        for trans in filtered_transactions:
            masked_card = get_mask_card_number(f"Карта {trans['from']}")
            masked_account = get_mask_account(trans['to'])
            print(
                f"\n{trans['date']} {trans['description']}\nСчет {masked_card} ➜ {masked_account}\nСумма: {trans['amount']} {trans['currency_code']}")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == '__main__':
    main()
