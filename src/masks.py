from typing import Union


def get_mask_card_number(full_cart_num: Union[str]) -> str:
    """Функция скрывает часть символов номера карты"""
    if full_cart_num.isdigit():
        return (
            f"{full_cart_num[0:4]} "
            f"{full_cart_num[4:6]}** **** {full_cart_num[-4:]}"
        )
    else:
        return 'Введен некорректный номер карты'


def get_mask_account(mask_account: Union[str]) -> str:
    """Функция скрывает часть символов номера счета"""

    if mask_account.isdigit():
        if len(mask_account) != 20:
            return 'Номера счета состоит из 20 символов'
        return f"**{mask_account[-4:]}"
    else:
        return 'Введен некорректный номер счета'
