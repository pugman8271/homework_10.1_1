from typing import Union

from src import masks


def mask_account_card(full_cart_name: Union[str]) -> str:
    """Функция скрывает часть символов номера карты/счета"""
    if "Счет" in full_cart_name:
        return f'Счет {masks.get_mask_account(full_cart_name[-20:])}'
    else:
        if len(full_cart_name.split()) == 3:
            return f"{full_cart_name.split()[-3]} {full_cart_name.split()[-2]} {masks.get_mask_card_number(full_cart_name.split()[-1])}"
        else:
            return f"{full_cart_name.split()[-2]} {masks.get_mask_card_number(full_cart_name.split()[-1])}"

def get_date(date_str: Union[str]) -> str:
    """Функция конвертирует дату"""
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
