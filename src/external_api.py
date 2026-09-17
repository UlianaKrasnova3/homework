import os

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
        try:
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

        except Exception as e:
            return "Произошла ошибка, проверьте данные"
