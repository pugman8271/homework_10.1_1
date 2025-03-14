import re
from collections import Counter
from typing import Union


def filter_by_state(dicts_list: Union[list], status_sorting: str = "EXECUTED") -> list:
    """Функция сортирует список словарей по необязательному параметру 'state',
    она принимает на вход список 'dicts_list', на выходе получаем отсортированный список
    """
    filtered_list = []
    for dict_i in dicts_list:
        if "state" in dict_i and dict_i["state"] == status_sorting:
            filtered_list.append(dict_i)
    return filtered_list


def sort_by_date(dicts_list: Union[list], sorting_method: bool = True) -> list:
    """Функция сортирует список словарей по дате в зависимости от необязательного параметра 'sorting_method',
    она принимает принимает на вход список 'dicts_list', на выходе получаем отсортированный список
    """
    sort_list = sorted(dicts_list, key=lambda x: x["date"], reverse=sorting_method)
    return sort_list


def sorting_by_amount(dicts_list, sorting_method):
    try:
        sort_list = sorted(
            dicts_list,
            key=lambda x: x["operationAmount"]["currency"]["code"],
            reverse=sorting_method,
        )
    except KeyError:
        sort_list = sorted(
            dicts_list, key=lambda x: x["amount"], reverse=sorting_method
        )
    return sort_list


def sort_by_currency(dicts_list, currency="RUB"):
    try:
        filtered_list = []
        for dict_i in dicts_list:
            if dict_i["operationAmount"]["currency"]["code"] == currency:
                filtered_list.append(dict_i)
    except IndexError:
        filtered_list = []
        for dict_i in dicts_list:
            if dict_i["currency_code"] == currency:
                filtered_list.append(dict_i)
    return filtered_list


def sort_by_keyword(dicts_list, keyword):
    """Функция для поиска в списке словарей операций по заданной строке — описанию"""

    searched_description = []
    pattern = re.compile(keyword.lower())
    for dicts in dicts_list:
        if "description" in dicts and re.search(pattern, dicts["description"].lower()):
            searched_description.append(dicts)
    return searched_description


def sort_by_category(dicts_list):
    """Функцию, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    operations_list = []
    for dicts in dicts_list:
        if dicts["description"] is not None:
            # Добавляем описание операции в список
            operations_list.append(dicts["description"])

    sorted_counter = Counter(operations_list)
    sorted_dict = dict(sorted_counter)
    return sorted_dict
