from src.masks import get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует информацию о картах и счетах"""
    parts = info.split()
    if len(parts) < 2:
        raise ValueError("Входные данные должны содержать название карты или счета и номер.")

    # Тип карты или счета
    type_card = " ".join(parts[:-1])
    # Получаем маскированный номер
    masked_number = get_mask_card_number(info)

    return f"{type_card} {masked_number}"


def get_date(date: str) -> str:
    """ДД.ММ.ГГГГ"""
    if not date:
        raise ValueError("Данные отсутствуют")
    else:
        try:
            # Разделяем строку на дату и время
            date_part = date.split("T")[0]

            # Разделяем дату на год, месяц и день
            year, month, day = date_part.split("-")

            # Форматируем дату в нужный формат
            formatted_date = f"{day}.{month}.{year}"
            return formatted_date

        except ValueError:
            return "Задан неверный формат"
