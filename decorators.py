import functools
from datetime import datetime

def during_start_of_minute(func):
    def wrapper(*args, **kwargs):
        actual_sec = datetime.now().second
        if 0 <= actual_sec < 30:
            func(*args, **kwargs)
        else:
            print(actual_sec)
    return wrapper

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
