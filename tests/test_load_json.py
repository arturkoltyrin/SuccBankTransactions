from unittest.mock import patch, mock_open
import json
from src.utils.load_json import load_transactions


def test_load_transactions_file_not_exist():
    """Тестирует ситуацию, когда файл не существует."""
    with patch('os.path.exists', return_value=False), \
         patch('os.path.isfile', return_value=False):
        result = load_transactions('fake_path.json')
        assert result == []


def test_load_transactions_file_not_a_file():
    """Тестирует ситуацию, когда путь не является файлом."""
    with patch('os.path.exists', return_value=True), \
         patch('os.path.isfile', return_value=False):
        result = load_transactions('fake_path.json')
        assert result == []


def test_load_transactions_empty_file():
    """Тестирует загрузку данных из пустого файла."""
    with patch('builtins.open', mock_open(read_data='')) as mock_file, \
         patch('os.path.exists', return_value=True), \
         patch('os.path.isfile', return_value=True):
        result = load_transactions('fake_path.json')
        assert result == []
        mock_file.assert_called_once_with('fake_path.json', 'r', encoding='utf-8')


def test_load_transactions_valid_json():
    """Тестирует загрузку данных из корректного JSON-файла."""
    transactions = [{'Amount': 100, 'Currency': 'USD'}]
    with patch('builtins.open', mock_open(read_data=json.dumps(transactions))) as mock_file, \
         patch('os.path.exists', return_value=True), \
         patch('os.path.isfile', return_value=True):
        result = load_transactions('fake_path.json')
        assert result == transactions
        mock_file.assert_called_once_with('fake_path.json', 'r', encoding='utf-8')


def test_load_transactions_invalid_json():
    """Тестирует ситуацию, когда JSON некорректен."""
    with patch('builtins.open', mock_open(read_data='invalid json')) as mock_file, \
         patch('os.path.exists', return_value=True), \
         patch('os.path.isfile', return_value=True):
        result = load_transactions('fake_path.json')
        assert result == []
        mock_file.assert_called_once_with('fake_path.json', 'r', encoding='utf-8')
