import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования функций.
    Логирует начало, конец выполнения функции и ее результаты и ошибки"""

    def decorator(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Определяем место, куда будем выводить логи
            if filename:
                log_output = open(filename, "a")
            else:
                log_output = None  # Вывод в консоль

            # Логируем начало функции
            if log_output:
                log_output.write(f"Запуск функции '{function.__name__}' с параметрами: {args}, {kwargs}")
            else:
                print(f"Запуск функции '{function.__name__}' с параметрами: {args}, {kwargs}")

            try:
                # Вызываем функцию
                result = function(*args, **kwargs)

                # Логируем успешное выполнение
                if log_output:
                    log_message = f"{function.__name__} успешно выполнилась"
                    log_output.write(log_message)
                else:
                    log_message = f"{function.__name__} успешно выполнилась"
                    print(log_message)
                return result

            except Exception as e:
                # Логируем ошибку
                error_message = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if log_output:
                    log_output.write(error_message)
                else:
                    print(error_message)

                raise

            finally:
                # Закрываем файл
                if log_output:
                    log_output.close()

        return wrapper

    return decorator
