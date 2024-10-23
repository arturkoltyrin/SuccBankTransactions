import pytest
from unittest.mock import patch
from src.reading_financial_transactions_from_CSV_XLSX_files.read_financ_transactions import load_transactions_from_csv, load_transactions_from_excel
import pandas as pd


csv_data = pd.DataFrame({
    'id': [650703, 3598919],
    'state': ['EXECUTED', 'EXECUTED'],
    'date': ['2023-09-05T11:30:32Z', '2020-12-06T23:00:58Z'],
    'amount': [16210, 29740],
    'currency_name': ['Sol', 'Peso'],
    'currency_code': ['PEN', 'COP'],
    'from': ['Счет 58803664561298323391', 'Discover 3172601889670065'],
    'to': ['Счет 39745660563456619397', 'Discover 0720428384694643'],
    'description': ['Перевод организации', 'Перевод с карты на карту']})


excel_data = pd.DataFrame({
    'id': [650703, 3598919],
    'state': ['EXECUTED', 'EXECUTED'],
    'date': ['2023-09-05T11:30:32Z', '2020-12-06T23:00:58Z'],
    'amount': [16210, 29740],
    'currency_name': ['Sol', 'Peso'],
    'currency_code': ['PEN', 'COP'],
    'from': ['Счет 58803664561298323391', 'Discover 3172601889670065'],
    'to': ['Счет 39745660563456619397', 'Discover 0720428384694643'],
    'description': ['Перевод организации', 'Перевод с карты на карту']})


def test_load_transactions_from_csv():
    with patch('pandas.read_csv', return_value=csv_data):
        result = load_transactions_from_csv('file.csv')
        expected_result = [
            {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
             'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
             'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
             'description': 'Перевод организации'},
            {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
             'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
             'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
             'description': 'Перевод с карты на карту'}]
        assert result == expected_result


def test_load_transactions_from_excel():
    with patch('pandas.read_excel', return_value=excel_data):
        result = load_transactions_from_excel('file.xlsx')
        expected_result = [
            {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
             'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
             'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
             'description': 'Перевод организации'},
            {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
             'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
             'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
             'description': 'Перевод с карты на карту'}]
        assert result == expected_result


def test_load_transactions_from_csv_exception():
    with patch('pandas.read_csv', side_effect=Exception("File not found")):
        with pytest.raises(Exception) as exc_info:
            load_transactions_from_csv('mock_file.csv')
        assert str(exc_info.value) == "Ошибка при считывании файла CSV: File not found"


def test_load_transactions_from_excel_exception():
    with patch('pandas.read_excel', side_effect=Exception("File not found")):
        with pytest.raises(Exception) as exc_info:
            load_transactions_from_excel('mock_file.xlsx')
        assert str(exc_info.value) == "Ошибка при считывании файла Excel: File not found"
