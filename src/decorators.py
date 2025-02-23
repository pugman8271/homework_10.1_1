import time
from datetime import datetime


def log(filename='mylog.txt'):
    def decorator_log(func):
        def wrapper(*args, **kwargs):
            try:
                star_func = datetime.now()
                result = func(*args, **kwargs)
                stop_func = datetime.now()
                total_time = (stop_func-star_func).seconds
                massage = (f"{func.__name__} ok \n"
                           f"Начало работы: {star_func}\n"
                           f"Конец работы {stop_func}\n")
                if not filename:
                    print(massage)
                else:
                    with open('mylog.txt', 'a',encoding='utf-8') as f:
                        f.write(massage)
                return result
            except Exception as a:
                massage = f"{func.__name__} {type(a).__name__} {args, kwargs}\n"
                if not filename:
                    print(massage)
                else:
                    with open('mylog.txt', 'a',encoding='utf-8') as f:
                        f.write(massage)
        return wrapper
    return decorator_log




if __name__ == "__main__":
    @log()
    def my_function(x, y):
        return x + y


    print(my_function(1, '3'))