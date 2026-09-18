import logging
import os
from typing import Union

current_dir = os.path.dirname(os.path.abspath(__file__))

logs_dir = os.path.abspath(os.path.join(current_dir, "../logs"))
os.makedirs(logs_dir, exist_ok=True)

rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number: Union[int, str]) -> str:
    '''
    Функция возвращает маску номера карты
    '''
    str_number = str(number)
    if len(str_number) == 16:
        result = str_number[:6] + "*" * 6 + str_number[-4:]
        logger.info(f'Возвращаем маску карты')
        return f"{result[:4]} {result[4:8]} {result[8:12]} {result[12:16]}"
    else:
        logger.error(f'Произошла ошибка, введен некорректный номер карты')
        return "Введен некорректный номер"


def get_mask_account(account: Union[int, str]) -> str:
    '''
    Функция возвращает маску номера аккаунта
    '''
    str_account = str(account)
    if len(str_account) >= 4:
        logger.info(f'Возвращаем маску номера аккаунта')
        return "**" + str_account[-4:]
    else:
        logger.error(f'Произошла ошибка, введен некорректный номер аккаунта')
        return "Введен некорректный номер"
