def filter_by_state(dicts_list):
    filtered_list = []
    for dict_i in dicts_list:
        if dict_i['state'] == 'EXECUTED':
            filtered_list.append(dict_i)
    return filtered_list



print(filter_by_state([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


