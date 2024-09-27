import pytest
from src.processing.processing import filter_by_state, sort_by_date


@pytest.fixture
def data_filter_by_state():
    return [
        {'state': 'EXECUTED', 'amount': 100},
        {'state': 'CANCELED', 'amount': 200},
        {'state': 'EXECUTED', 'amount': 300},]


def test_filter_by_state(data_filter_by_state):

    # Тестирование фильтрации по state
    assert filter_by_state(data_filter_by_state, 'EXECUTED') == [
        {'state': 'EXECUTED', 'amount': 100},
        {'state': 'EXECUTED', 'amount': 300}]

    # Тестирование отсутствия словарей с указанным state
    assert filter_by_state(data_filter_by_state, 'ANOTHER_KEY') == []


@pytest.fixture
def date_sample_sort_by_date():
    return [
        {'date': '2023-10-10', 'amount': 100},
        {'date': '2023-10-12', 'amount': 200},
        {'date': '2023-10-11', 'amount': 300},]

def test_sort_by_date(date_sample_sort_by_date):

    # Сортировка по дате по возрастанию
    assert sort_by_date(date_sample_sort_by_date) == [
        {'date': '2023-10-10', 'amount': 100},
        {'date': '2023-10-11', 'amount': 300},
        {'date': '2023-10-12', 'amount': 200}]

    # Сортировка по дате по убыванию
    assert sort_by_date(date_sample_sort_by_date, reverse=True) == [
        {'date': '2023-10-12', 'amount': 200},
        {'date': '2023-10-11', 'amount': 300},
        {'date': '2023-10-10', 'amount': 100}]