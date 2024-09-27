def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры."""

    # Разделение входной строки на части
    parts = card_number.split()

    # Проверка, что входная строка содержит как минимум тип и номер
    if len(parts) < 2:
        raise ValueError("Входные данные должны содержать название карты или счета и номер.")

    # Объединяем все части, кроме последней в тип
    type_card = " ".join(parts[:-1])
    number = parts[-1]  # Последний элемент - это номер

    if "Счет" in type_card:
        # Если тип - счет, маскируем номер
        return f"{type_card} **{number[-4:]}"
    else:
        # Если это карта, маскируем номер карты
        if len(number) > 10:
            vis_part = number[:6] + number[-4:]
            masked_part = "*" * (len(number) - 10)
            masked_card_number = f"{vis_part[:4]} {vis_part[4:6]}{masked_part[:2]} {masked_part[:4]} {vis_part[-4:]}"
            return f"{type_card} {masked_card_number}"
        else:
            # Обработать случай с номером карты, меньше или равным 10 символам
            return f"{type_card} {number}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми последние 4 цифры."""

    return f"**{account_number[-4:]}"
