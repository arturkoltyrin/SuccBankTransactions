import pytest
from src.widget.mask_account_card import get_date, mask_account_card


@pytest.mark.parametrize("input_date, exit_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-01-01T02:26:18.671407", "01.01.2023"),])


def test_get_date(input_date, exit_output):
    assert get_date(input_date) == exit_output


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("Данные отсутствуют")

@pytest.mark.parametrize("input_card, exit_output", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305")])


def test_mask_account_card(input_card, exit_output):
    assert mask_account_card(input_card) == exit_output
