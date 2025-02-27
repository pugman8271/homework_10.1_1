import json
import os


def operations_json_get_info(directory):
    try:
        with open('..'+directory, encoding='utf-8') as f:
            return json.load(f)
    except:
        return []





