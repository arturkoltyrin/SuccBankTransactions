import pytest

from src.decorators.decorators import log


@log()
def add(a, b):
    return a + b


@log()
def divide(a, b):
    return a / b


@log()
def raise_exception():
    raise ValueError("Some error occurred")


def test_add_function_success(capsys):
    result = add(3, 4)

    # захватываем вывод
    captured = capsys.readouterr()

    assert result == 7
    assert "Запуск функции 'add' с параметрами: (3, 4), {}" in captured.out
    assert "add успешно выполнилась" in captured.out


def test_divide_function_success(capsys):
    result = divide(10, 2)

    # захватываем вывод
    captured = capsys.readouterr()

    assert result == 5
    assert "Запуск функции 'divide' с параметрами: (10, 2), {}" in captured.out
    assert "divide успешно выполнилась" in captured.out


def test_divide_function_zero_division(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # захватываем вывод
    captured = capsys.readouterr()

    assert "Запуск функции 'divide' с параметрами: (10, 0), {}" in captured.out
    assert "divide error: ZeroDivisionError. Inputs: (10, 0), {}" in captured.out


def test_raise_exception(capsys):
    with pytest.raises(ValueError, match="Some error occurred"):
        raise_exception()

    # захватываем вывод
    captured = capsys.readouterr()

    assert "Запуск функции 'raise_exception' с параметрами: (), {}" in captured.out
    assert "raise_exception error: ValueError. Inputs: (), {}" in captured.out
