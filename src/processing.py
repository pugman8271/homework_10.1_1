from typing import Union


def filter_by_state(dicts_list: Union[list], status_sorting: str="EXECUTED") -> list:
    """Функция сортирует список словарей по необязательному параметру 'state',
    она принимает на вход список 'dicts_list', на выходе получаем отсортированный список
    """
    filtered_list = []
    for dict_i in dicts_list:
        if dict_i["state"] == status_sorting:
            filtered_list.append(dict_i)
    return filtered_list


def sort_by_date(dicts_list: Union[list], sorting_method:bool =True) -> list:
    """Функция сортирует список словарей по дате в зависимости от необязательного параметра 'sorting_method',
    она принимает принимает на вход список 'dicts_list', на выходе получаем отсортированный список
    """
    sort_list = sorted(dicts_list, key=lambda x: x["date"], reverse=sorting_method)
    return sort_list

