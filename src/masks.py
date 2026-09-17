import logging
import os
from typing import Union

logs_path = 'logs'
os.makedirs(logs_path, exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Users/User/PycharmProjects/homework/logs/masks.log", encoding='utf-8')
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
