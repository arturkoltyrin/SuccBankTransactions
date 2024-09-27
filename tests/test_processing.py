import pytest
from src.processing.processing import filter_by_state


@pytest.fixture
def sample_data():
    return [
        {'state': 'EXECUTED', 'amount': 100},
        {'state': 'CANCELED', 'amount': 200},
        {'state': 'EXECUTED', 'amount': 300},]


def test_filter_by_state(sample_data):

    # Тестирование фильтрации по state
    assert filter_by_state(sample_data, 'EXECUTED') == [
        {'state': 'EXECUTED', 'amount': 100},
        {'state': 'EXECUTED', 'amount': 300}]

    # Тестирование отсутствия словарей с указанным state
    assert filter_by_state(sample_data, 'ANOTHER_KEY') == []
