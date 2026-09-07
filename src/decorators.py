from functools import wraps
from time import time


def log(filename=None):
    '''
    Декоратор 'log' принимает необязательный аргумент 'filename',
    который определяет имя файла, в который будут записываться логи
    '''

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start = time()
            error = None
            result = None
            try:
                result = func(*args, **kwargs)
                status = "ok"
            except Exception as e:
                error = str(e)
                status = "error"
                raise
            finally:
                end = time()
                time_work = end - start

                if filename:
                    with open(filename, 'a', encoding="UTF-8") as f:
                        f.write(f'Time work: {time_work}\n')

                        if status == "ok":
                            f.write(f"{func.__name__}: {status}\n")
                        else:
                            f.write(f"{func.__name__} {type(error).__name__}: {error}. Inputs: {args}, {kwargs}")
                else:
                    print(f'Time work: {time_work}\n')

                    if status == "ok":
                        print(f"{func.__name__}: {status}")
                    else:
                        print(f"{func.__name__} {type(error).__name__}: {error}. Inputs: {args}, {kwargs}")

            return result

        return inner

    return wrapper
