from datetime import datetime
from decorators import during_start_of_minute, do_twice

@do_twice
def say_whee():
    print(f"Wheeee! {datetime.now().second}")

@do_twice
def greet(name):
    print(f"Hi {name}! How are yo doing?")

if __name__ == '__main__':
    g = greet("Jorge")
    s = say_whee()
