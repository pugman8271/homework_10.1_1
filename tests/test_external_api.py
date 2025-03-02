import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import convert_transaction

load_dotenv(".env")


API_KEY_apilayer = os.getenv("API_KEY_apilayer")


@patch("requests.get")
def test_convert_transaction(mock_get):
    mock_get.return_value.json.return_value = {"success": True, "result": "result_test"}
    assert (
        convert_transaction(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "test_data",
                "operationAmount": {
                    "amount": "test_amount",
                    "currency": {"name": "руб.", "code": "usd"},
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == "result_test"
    )
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=rub&from=usd&amount=test_amount",
        headers={"apikey": API_KEY_apilayer},
        data={},
    )
