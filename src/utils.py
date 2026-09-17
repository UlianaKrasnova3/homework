import json
import logging
import os

logs_path = 'logs'

os.makedirs(logs_path, exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Users/User/PycharmProjects/homework/logs/utils.log", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def fin_transaction(json_file_name: str) -> list:
    '''Возвращает данные о финансовых транзакциях'''
    try:
        logger.info(f'Открываем файл {json_file_name}')
        path = os.path.join('..', 'data', json_file_name)
        with open(path, 'r', encoding='utf-8') as f:
            list_fin_transaction = json.load(f)
        return list_fin_transaction

    except Exception as e:
        logger.error(f'Произошла ошибка {e}')
        return []
