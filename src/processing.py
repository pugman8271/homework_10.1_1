from typing import Union


def filter_by_state(dicts_list: Union[list]) -> list:
    filtered_list = []
    for dict_i in dicts_list:
        if dict_i['state'] == 'EXECUTED':
            filtered_list.append(dict_i)
    return filtered_list




def sort_by_date(dicts_list: Union[list], reverse=True) -> list:
    return sorted(dicts_list, key=lambda x: x['date'], reverse=reverse)

