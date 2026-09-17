import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import conversion

load_dotenv()

API_KEY = os.getenv("API_KEY")


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
