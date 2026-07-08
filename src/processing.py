def filter_by_state(list_of_dicts: list, state='EXECUTED') -> list:
    '''
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state
 соответствует указанному значению.
 '''

    new_list_of_dicts = []
    for item in range(len(list_of_dicts)):
        if list_of_dicts[item]['state'] == state:
            new_list_of_dicts.append(list_of_dicts[item])
    return new_list_of_dicts


def sort_by_date(list_of_dicts: list, user_reverse: bool = True) -> list:
    '''
    Функция возвращает новый список, отсортированный по дате
    '''
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x['date'], reverse=user_reverse)
    return sorted_list_of_dicts
