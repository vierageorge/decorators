from datetime import datetime

def during_start_of_minute(func):
    def wrapper():
        actual_sec = datetime.now().second
        if 0 <= actual_sec < 30:
            func()
        else:
            print(actual_sec)
    return wrapper

def say_whee():
    print(f"Wheeee! {datetime.now().second}")

say_whee = during_start_of_minute(say_whee)
say_whee()
