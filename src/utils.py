import json


def operations_json_get_info(directory):
    """Функция получения содержимого из .json файла"""
    try:
        with open(directory, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []
