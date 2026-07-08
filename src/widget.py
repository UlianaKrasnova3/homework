from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    '''
    Функция возвращает маску номера карты и названия
    '''
    try:
        for item in account_card:
            mask = ''
            if account_card[:4] == 'Счет':
                mask = 'Счет ' + get_mask_account(account_card[5:])
            else:
                parts = account_card.split()
                card_number = parts[-1]
                card_name = ' '.join(parts[:-1])
                mask_card_number = get_mask_card_number(card_number)
                if mask_card_number == "Введен некорректный номер":
                    return "Введен некорректный номер"
                mask = card_name + ' ' + mask_card_number
        return mask
    except UnboundLocalError:
        print("Введен некорректный номер")


def get_date(date: str) -> str:
    '''
    Функция форматирует дату
    '''
    def date_separator(String: str, separator: str):
        try:
            first_index = String.index(separator)
            second_index = String.index(separator, first_index + 1)
            # проверяем правда ли separator разделяет дату, а не другие числа
            if second_index - first_index == 3:
                # ищем, каким индексом заканчивается дата
                data_end = second_index + 1
                while String[data_end].isdigit():
                    if data_end == len(String) - 1:
                        break
                    data_end += 1
                if data_end != len(String) - 1:
                    data_end -= 1
                # проверяем начинается ли дата с года или заканчивается им
                if data_end - second_index == 2:
                    # дата начинается с года
                    year = String[first_index - 4:first_index]
                    month = String[first_index + 1:second_index]
                    day = String[second_index + 1:data_end + 1]
                # если дата заканчивается годом
                elif data_end - second_index == 4:
                    day = String[first_index - 2:first_index]
                    month = String[first_index + 1:second_index]
                    year = String[second_index + 1:data_end + 1]

                return f'{day}{separator}{month}{separator}{year}'
            else:
                return 'Дата не распознана'
        except Exception:
            return 'Дата не распознана'

    try:
        # если дата разделена знаком "/"
        if '/' in date:
            date_formated = date_separator(date, '/')
        # если дата разделена знаком "-"
        elif '-' in date:
            date_formated = date_separator(date, '-')
        # если дата разделена знаком "."
        elif date.count('.') > 1:
            date_formated = date_separator(date, '.')

        return date_formated
    except Exception:
        return 'Дата не распознана'
