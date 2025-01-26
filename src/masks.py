from typing import Union


def get_mask_card_number(full_cart_num: Union[str]) -> str:
    """Функция скрывает часть символов номера карты"""

    return (
        f"{full_cart_num[:-17]} {full_cart_num[-16:-12]} "
        f"{full_cart_num[-12:-10]}** **** {full_cart_num[-4:]}"
    )


def get_mask_account(mask_account: Union[str]) -> str:
    """Функция скрывает часть символов номера счета"""

    return f"{mask_account[:-21]} **{mask_account[-4:]}"
