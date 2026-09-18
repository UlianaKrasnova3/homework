import json
import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

logs_dir = os.path.abspath(os.path.join(current_dir, "../logs"))
os.makedirs(logs_dir, exist_ok=True)

rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, encoding='utf-8')
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
