from typing import Union


def get_mask_card_number(number: Union[int, str]) -> str:
    '''
    Функция возвращает маску номера карты
    '''
    str_number = str(number)
    if len(str_number) == 16:
        result = str_number[:6] + "*" * 6 + str_number[-4:]
        return f"{result[:4]} {result[4:8]} {result[8:12]} {result[12:16]}"


def get_mask_account(account: Union[int, str]) -> str:
    '''
    Функция возвращает маску номера аккаунта
    '''
    str_account = str(account)
    if len(str_account) >= 4:
        return "**" + str_account[-4:]
