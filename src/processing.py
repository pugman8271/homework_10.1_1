from os.path import isabs
from typing import Union
import re

def filter_by_state(dicts_list: Union[list], status_sorting: str = "EXECUTED") -> list:
    """Функция сортирует список словарей по необязательному параметру 'state',
    она принимает на вход список 'dicts_list', на выходе получаем отсортированный список
    """
    filtered_list = []
    for dict_i in dicts_list:
        if 'state' in dict_i and dict_i['state'] == status_sorting:
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
        sort_list = sorted(dicts_list, key=lambda x: x["operationAmount"]["currency"]["code"], reverse=sorting_method)
    except:
        sort_list = sorted(dicts_list, key=lambda x: x["amount"], reverse=sorting_method)
    return sort_list

def sort_by_currency(dicts_list, currency = 'RUB'):
    try:
        filtered_list = []
        for dict_i in dicts_list:
            if dict_i['operationAmount']["currency"]["code"] == currency:
                filtered_list.append(dict_i)
    except:
        filtered_list = []
        for dict_i in dicts_list:
            if dict_i['currency_code'] == currency:
                filtered_list.append(dict_i)

    return filtered_list



def sort_by_description(dicts_list):
    pass



