def filter_by_currency(list_of_dicts, currency):
    '''
    Генераторная функция, которая возвращает итератор,
    поочередно выдающий транзакции,
    где валюта операции соответствует заданной
    '''
    i = 0
    while i < len(list_of_dicts):
        if list_of_dicts[i]["operationAmount"]["currency"]["code"] == currency:
            yield list_of_dicts[i]
        i += 1


def transaction_descriptions(list_of_dicts):
    '''
    Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди
    '''
    i = 0
    while i < len(list_of_dicts):
        yield list_of_dicts[i]["description"]
        i += 1


def card_number_generator(start, stop):
    '''
    Функция генерирует номера карт в заданном диапазоне
    '''
    if start > stop:
        start, stop = stop, start
    for i in range(start, stop + 1):
        card_number = str(i)
        while len(card_number) < 16:
            card_number = '0' + card_number
        yield f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}'
