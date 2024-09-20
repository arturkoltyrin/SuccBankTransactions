from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
   parts = info.split()
   if len(parts) < 2:
       raise ValueError("Input must have both type and number.")

   type_ = parts[0]
   number = parts[1]

   if "Счет" in type_:
       return get_mask_account(number)
   else:
       return get_mask_card_number(number)
