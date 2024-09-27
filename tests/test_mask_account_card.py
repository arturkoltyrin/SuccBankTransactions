import pytest
from src.widget.mask_account_card import get_date


@pytest.mark.parametrize("input_date, exit_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-01-01T02:26:18.671407", "01.01.2023"),])


def test_get_date(input_date, exit_output):
    assert get_date(input_date) == exit_output


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("date_invalid")
