def log(filename='mylog.txt'):
    def log_massage(massage):
        if filename is None:
            print(massage)
        else:
            with open('mylog.txt', 'a', encoding='utf-8') as f:
                f.write(massage)
    def decorator_log(func):
        def wrapper(*args, **kwargs):
            try:

                result = func(*args, **kwargs)
                massage = (f"{func.__name__} ok \n")
                log_massage(massage)

                return result
            except Exception as a:
                massage = f"Ошибка {func.__name__} {type(a).__name__} {args, kwargs}\n"
                log_massage(massage)
                raise a

        return wrapper
    return decorator_log




if __name__ == "__main__":
    @log(filename='mylog.txt')
    def my_function(x, y):
        return x + y


    print(my_function(2, 5))