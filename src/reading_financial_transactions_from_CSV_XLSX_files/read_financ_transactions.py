from typing import Dict, List
import os
import pandas as pd
import openpyxl


def load_transactions_from_csv(filepath: str = "C:/Users/user/PycharmProjects/SuccBankTransactions/data/transactions_csv.csv") -> List[Dict[str, str]]:
    """Считывает финансовые операции из файла CSV."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Файл не найден: {filepath}")

    try:
        # Читаем CSV файл с табуляцией как разделителями
        data = pd.read_csv(filepath, sep=';', encoding='utf-8')

        # Проверка заголовков
        print(data.head())  # Печать первых 5 строк данных
        print(data.columns.tolist())  # Печать названий колонок

        transactions = data.to_dict(orient="records")

        # Возвращаем список словарей с необходимыми полями
        return [{
            'id': str(t['id']),
            'state': t['state'],
            'date': t['date'],
            'amount': str(t['amount']),
            'currency_name': t['currency_name'],
            'currency_code': t['currency_code'],
            'from': t['from'],
            'to': t['to'],
            'description': t['description']} for t in transactions]

    except Exception as e:
        raise Exception(f"Ошибка при считывании файла CSV: {e}")


def load_transactions_from_excel(
        filepath: str = "C:/Users/user/PycharmProjects/SuccBankTransactions/data/transactions_excel.xlsx") -> List[
    Dict[str, str]]:
    """Считывает финансовые операции из файла Excel."""
    try:
        data = pd.read_excel(filepath)

        # Удаляем пробелы в заголовках
        data.columns = data.columns.str.strip()

        # Проверка на наличие нужных заголовков
        required_columns = ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to',
                            'description']
        for column in required_columns:
            if column not in data.columns:
                raise KeyError(f"Отсутствует колонка: {column}")

        # Заполняем пропуски
        data = data.fillna('')

        transactions = data.to_dict(orient="records")
        return [{'id': str(t['id']),
                 'state': t['state'],
                 'date': t['date'],
                 'amount': str(t['amount']),
                 'currency_name': t['currency_name'],
                 'currency_code': t['currency_code'],
                 'from': t['from'],
                 'to': t['to'],
                 'description': t['description']} for t in transactions]
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
    except KeyError as e:
        print(f"Ошибка ключа: {e}")
    except Exception as e:
        print(f"Ошибка при считывании файла Excel: {e}")
