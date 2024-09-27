from datetime import datetime

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



def get_date(date_str: str) -> str:
   """ДД.ММ.ГГГГ"""
   dt = datetime.fromisoformat(date_str)

   return dt.strftime("%d.%m.%Y")
