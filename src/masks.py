from typing import Union


def add_spaces(text: Union[str]) -> str:
    """Функция добавляет пробелы через каждые 4 символа"""
    result = ""
    for i in range(0, len(text), 4):
        if i > 0:
            result += " "
        result += text[i : i + 4]
    return result


def get_mask_card_number(full_cart_num: Union[int]) -> str:
    """Функция скрывает часть символов номера карты"""
    print_number_cart = ""
    full_cart_num_str = str(full_cart_num)
    if len(full_cart_num_str) != 16:
        print("Номер карты введен некорректно")
    else:
        for num in range(16):
            if 5 < num < 12:
                print_number_cart += "*"
            else:
                print_number_cart += full_cart_num_str[num]
    return add_spaces(print_number_cart)


def get_mask_account(mask_account: Union[int]) -> str:
    """Функция скрывает часть символов номера счета"""
    print_mask_account = ""
    mask_account_str = str(mask_account)
    if len(mask_account_str) != 20:
        print("Номер счета введен некорректно")
    else:
        for num in range(14, 20):
            if 0 < num < 16:
                print_mask_account += "*"
            else:
                print_mask_account += mask_account_str[num]
    return print_mask_account
