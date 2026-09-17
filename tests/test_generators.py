from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, transactions_2):
    generator = filter_by_currency(transactions, "USD")
    assert (next(generator)) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
    assert (next(generator)) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"}

    assert (next(generator)) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"}
    generator_2 = filter_by_currency(transactions_2, "USD")
    try:
        next(generator_2)
        assert False, "Expected StopIteration"
    except StopIteration:
        pass
    generator_3 = filter_by_currency([], "USD")
    try:
        next(generator_3)
        assert False, "Expected StopIteration"
    except StopIteration:
        pass


def test_transaction_descriptions(transactions, transactions_3):
    generator = transaction_descriptions(transactions)
    assert (next(generator)) == "Перевод организации"
    assert (next(generator)) == "Перевод со счета на счет"
    assert (next(generator)) == "Перевод со счета на счет"
    assert (next(generator)) == "Перевод с карты на карту"
    assert (next(generator)) == "Перевод организации"
    generator_2 = transaction_descriptions([])
    try:
        next(generator_2)
        assert False, "Expected StopIteration"
    except StopIteration:
        pass
    generator_3 = transaction_descriptions(transactions_3)
    assert (next(generator_3)) == "-"
    assert (next(generator_3)) == "Перевод организации"
    assert (next(generator_3)) == "--"


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert (next(generator)) == '0000 0000 0000 0001'
    assert (next(generator)) == '0000 0000 0000 0002'
    assert (next(generator)) == '0000 0000 0000 0003'
    assert (next(generator)) == '0000 0000 0000 0004'
    assert (next(generator)) == '0000 0000 0000 0005'
    generator_2 = card_number_generator(9999999999999990, 9999999999999999)
    assert (next(generator_2)) == '9999 9999 9999 9990'
    assert (next(generator_2)) == '9999 9999 9999 9991'
    assert (next(generator_2)) == '9999 9999 9999 9992'
    assert (next(generator_2)) == '9999 9999 9999 9993'
    assert (next(generator_2)) == '9999 9999 9999 9994'
    assert (next(generator_2)) == '9999 9999 9999 9995'
    assert (next(generator_2)) == '9999 9999 9999 9996'
    assert (next(generator_2)) == '9999 9999 9999 9997'
    assert (next(generator_2)) == '9999 9999 9999 9998'
    assert (next(generator_2)) == '9999 9999 9999 9999'
    generator_3 = card_number_generator(12340, 12336)
    assert (next(generator_3)) == '0000 0000 0001 2336'
    assert (next(generator_3)) == '0000 0000 0001 2337'
    assert (next(generator_3)) == '0000 0000 0001 2338'
    assert (next(generator_3)) == '0000 0000 0001 2339'
    assert (next(generator_3)) == '0000 0000 0001 2340'
    generator_4 = card_number_generator(12345678, 12345678)
    assert (next(generator_4)) == '0000 0000 1234 5678'
