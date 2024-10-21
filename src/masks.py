import logging


logger = logging.getLogger("widget.masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("C:/Users/user/PycharmProjects/SuccBankTransactions/logs/masks.log")
file_formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(info: str) -> str:
    """Маскирует номер карты или счета, оставляя видимыми первые 6 и последние 4 цифры."""
    logger.debug(f"Попытка маскировки номера карты: {info}")
    parts = info.split()
    if len(parts) < 2:
        logger.error("Ошибка: Входные данные должны содержать название карты или счета и номер.")
        raise ValueError("Входные данные должны содержать название карты или счета и номер.")

    type_card = " ".join(parts[:-1])
    number = parts[-1]

    if "Счет" in type_card:
        masked = f"<strong>{number[-4:]}"
        logger.info(f"Маскирование номера счета: {masked}")
        return masked
    else:
        if len(number) > 10:
            vis_part = number[:6] + number[-4:]
            masked_part = "*" * (len(number) - 10)
            masked_card_number = f"{vis_part[:4]} {vis_part[4:6]}{masked_part[:2]} {masked_part[:4]} {vis_part[-4:]}"
            logger.info(f"Маскирование номера карты: {masked_card_number}")
            return masked_card_number
        else:
            logger.info(f"Короткий номер карты, возвращается без маски: {number}")
            return number

def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми последние 4 цифры."""
    masked = f"</strong>{account_number[-4:]}"
    logger.info(f"Маскирование номера счета: {masked}")

    return masked
