import os
from unittest.mock import patch

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def conversion(transaction: dict) -> float:
    '''
    Функция возвращает сумму транзакции и при необходимости конвертирует ее в рубли
    '''
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]

        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {
            "amount": amount,
            "from": currency,
            "to": "RUB"
        }

        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url, headers=headers, params=payload)

        result = response.json()

        return result["result"]


@patch('requests.get')
def test_conversion(mock_get):
    mock_get.return_value.json.return_value = {"result": 1}
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }
    assert conversion(transaction) == 1
    mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert',
                                     headers={"apikey": API_KEY},
                                     params={
                                         "amount": "100.0",
                                         "from": "USD",
                                         "to": "RUB"
                                     })
