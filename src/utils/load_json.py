import json
import os
import logging
from typing import List, Dict, Any


logger = logging.getLogger("utils.load_json")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("C:/Users/user/PycharmProjects/SuccBankTransactions/logs/load_json.log")
file_formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(filepath: str) -> List[Dict[str, Any]]:
    """Загружает финансовые транзакции из JSON-файла."""
    logger.debug(f"Попытка загрузить файл: {filepath}")
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        logger.error(f"Файл не найден или не является файлом: {filepath}")
        return []

    with open(filepath, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Файл успешно загружен.")
                return data
            logger.warning("Данные в файле не являются списком.")
            return []
        except (json.JSONDecodeError, TypeError) as e:
            logger.error(f"Ошибка декодирования JSON: {e}")

            return []
