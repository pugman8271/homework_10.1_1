import os

import requests
from dotenv import load_dotenv

from src import utils

load_dotenv(".env")

API_KEY_apilayer = os.getenv("API_KEY_apilayer")

transaction_list = utils.operations_json_get_info("/data/operations.json")


def convert_transaction(transaction):
    """Функция конвертации валюты, полученной из информации о транзакции"""
    try:
        currency_to = "rub"
        currency_from = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to="
            f"{currency_to}&from={currency_from}&amount={amount}"
        )
        payload = {}
        headers = {"apikey": API_KEY_apilayer}
        response = requests.get(url, headers=headers, data=payload)
        return float(response.json()["result"])
    except Exception:
        return "Что-то пошло не так"
