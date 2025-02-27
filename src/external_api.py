from src import utils
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')

API_KEY_apilayer = os.getenv('API_KEY_apilayer')

transaction_list = utils.operations_json_get_info("/data/operations.json")


def convert_transaction(transaction):
    try:
        currency_to = 'RUB'
        currency_from = transaction['operationAmount']['currency']['code']
        amount = float(transaction['operationAmount']['amount'])
        url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
               f"{currency_to}&from={currency_from}&amount={amount}")
        payload = {}
        headers = {
            "apikey": API_KEY_apilayer
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response
        return f'{json.loads(result.text)['query']['amount']} RUB'
    except Exception:
        return 'Что-то пошло не так'


print((convert_transaction({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
})))
