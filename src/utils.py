import json
import os


def fin_transaction(json_file_name: str) -> list:
    '''Возвращает данные о финансовых транзакциях'''
    try:
        path = os.path.join('..', 'data', json_file_name)
        with open(path, 'r', encoding='utf-8') as f:
            list_fin_transaction = json.load(f)
        return list_fin_transaction

    except Exception as e:
        return []

# print (fin_transaction('operations.json'))
