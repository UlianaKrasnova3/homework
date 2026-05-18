from typing import Union
from masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    for item in account_card:
        mask = ''
        if account_card[:4] == 'Счет':
            mask = 'Счет **' + account_card[-4:]
        else:
            card_name = ''
            card_number = ''
            for i in account_card:
                if i.isalpha():
                    card_name += i
                elif i.isdigit():
                    card_number += i
            mask_card_number = get_mask_card_number(card_number)
            mask = card_name + ' ' + mask_card_number
    return mask


