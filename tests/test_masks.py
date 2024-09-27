import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input_card_number, exit_output",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("Счет 64686473678894779589", "**9589"),
        ("Master Card 7158300734726758", "7158 30** **** 6758"),
        ("Счет 35383033474447895560", "**5560"),
        ("Visa Classic 6831982476737658", "6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "5999 41** **** 6353"),
        ("Счет 73654108430135874305", "**4305"),
    ],
)
def test_get_mask_card_number(input_card_number, exit_output):
    if input_card_number and exit_output:
        assert get_mask_card_number(input_card_number) == exit_output
    else:
        if input_card_number is False or exit_output is False:
            with pytest.raises(ValueError):
                get_mask_card_number("Входные данные должны содержать название карты или счета и номер.")


@pytest.mark.parametrize(
    "input_account_number, exit_output",
    [
        ("73654108430135874305", "**4305"),
        ("84930254671289437564", "**7564"),
        ("01375829463012894716", "**4716"),
        ("56724938012564738901", "**8901"),
        ("48293061720574893475", "**3475"),
        ("10394857628491627384", "**7384"),
        ("29483756102837461593", "**1593"),
        ("47658291346965078321", "**8321"),
        ("36891254700812398765", "**8765"),
        ("72203456812980437512", "**7512"),
    ],
)
def test_get_mask_account(input_account_number, exit_output):
    assert get_mask_account(input_account_number) == exit_output
