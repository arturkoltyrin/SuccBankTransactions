from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(info: str) -> str:
   parts = info.split()
   if len(parts) < 2:
       raise ValueError("Input must have both type and number.")
   elif len(parts) == 2:
       type_ = parts[0]
       number = parts[1]
       if "Счет" in type_:
           return get_mask_account(number)
       else:
           return get_mask_card_number(number)
   elif len(parts) > 2:
       type_ = parts[0]
       number = parts[2]
       if "Visa" in type_:
           return get_mask_card_number(number)

def get_date(date_str: str) -> str:
   dt = datetime.fromisoformat(date_str)

   return dt.strftime("%d.%m.%Y")

print(mask_account_card('Счет 73654108430135874305'))