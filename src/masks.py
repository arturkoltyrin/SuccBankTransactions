def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры."""
    vis_part = card_number[:6] + card_number[-4:]
    masked_part = "*" * (len(card_number) - 10)
    masked_card_number = f"{vis_part[:4]} {vis_part[4:6]}{masked_part[:2]} {masked_part[:4]} {vis_part[-4:]}"

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми последние 4 цифры."""

    return f"**{account_number[-4:]}"
