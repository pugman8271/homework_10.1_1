from typing import Union


def mask_account_card(full_cart_name: Union[str]) -> str:
    """Функция скрывает часть символов номера карты/счета"""
    if "Счет" in full_cart_name:
        return f"{full_cart_name[:4]} **{full_cart_name[-4:]}"
    else:

        return (f"{full_cart_name[:-17]} {full_cart_name[-16:-12]} "
                f"{full_cart_name[-12:-10]}** **** {full_cart_name[-4:]}")


def get_date(date_str: Union[str]) -> str:
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"


