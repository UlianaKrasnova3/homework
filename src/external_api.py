import os

import requests
from dotenv import load_dotenv

import logging

logger = logging.getLogger("external_api")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Users/User/PycharmProjects/homework/logs/external_api.log", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

load_dotenv()

API_KEY = os.getenv("API_KEY")


def conversion(transaction: dict) -> float:
    '''
    Функция возвращает сумму транзакции и при необходимости конвертирует ее в рубли
    '''
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger.info(f'Получаем сумму транзакции в рублях')
        return transaction["operationAmount"]["amount"]
    else:
        try:
            logger.info(f'Получаем сумму транзакции через API и переводим в рубли')
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
            logger.error(f'Произошла ошибка {e}')
            return "Произошла ошибка, проверьте данные"
