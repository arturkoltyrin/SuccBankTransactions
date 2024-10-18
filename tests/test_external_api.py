from unittest.mock import patch, MagicMock
from src.external_api.external_api import convert_to_rub
from dotenv import load_dotenv

# Загружаем переменные окружения перед запусками тестов
load_dotenv(".env")


def test_convert_to_rub_currency_rub():
    """Тестирует конвертацию, если валюта в рублях."""
    transaction = {"operationAmount": {"amount": 150.0, "currency": {"code": "RUB"}}}
    result = convert_to_rub(transaction)
    assert result == 150.0, f"Expected 150.0 but got {result}"


def test_convert_to_rub_successful_conversion():
    """Тестирует успешную конвертацию из USD в RUB."""
    transaction = {"operationAmount": {"amount": 150.0, "currency": {"code": "USD"}}}
    with patch("requests.get") as mock_get, patch("os.getenv", return_value="fake_api_key"):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 12000.0}
        mock_get.return_value = mock_response

        result = convert_to_rub(transaction)
        assert result == 12000.0, f"Expected 12000.0 but got {result}"


def test_convert_to_rub_failed_conversion():
    """Тестирует обработку ошибки при запросе на API."""
    transaction = {"operationAmount": {"amount": 150.0, "currency": {"code": "EUR"}}}
    with patch("requests.get") as mock_get, patch("os.getenv", return_value="fake_api_key"):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        result = convert_to_rub(transaction)
        assert result == 0.0, f"Expected 0.0 but got {result}"


def test_convert_to_rub_invalid_response():
    """Тестирует случай, когда API возвращает некорректный ответ."""
    transaction = {"operationAmount": {"amount": 150.0, "currency": {"code": "JPY"}}}
    with patch("requests.get") as mock_get, patch("os.getenv", return_value="fake_api_key"):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        result = convert_to_rub(transaction)
        assert result == 0.0, f"Expected 0.0 but got {result}"
