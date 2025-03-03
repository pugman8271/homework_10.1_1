import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(full_cart_num: Union[str]) -> str:
    """Функция скрывает часть символов номера карты"""
    if full_cart_num.isdigit():
        logger.info(f"Был получен замаскированный номер карты {get_mask_card_number}")
        return (
            f"{full_cart_num[0:4]} " f"{full_cart_num[4:6]}** **** {full_cart_num[-4:]}"
        )
    else:
        logger.info(f"Неккоректно введен {full_cart_num}")
        return "Введен некорректный номер карты"


def get_mask_account(mask_account: Union[str]) -> str:
    """Функция скрывает часть символов номера счета"""

    if mask_account.isdigit():
        if len(mask_account) != 20:
            logger.info(f"Неккоректно введен {mask_account}")
            return "Номера счета состоит из 20 символов"
        logger.info(f"Был получен замаскированный номер счета {mask_account}")
        return f"**{mask_account[-4:]}"
    else:
        logger.info(f"Неккоректно введен {mask_account}")
        return "Введен некорректный номер счета"
