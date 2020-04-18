from datetime import datetime
from decorators import during_start_of_minute

@during_start_of_minute
def say_whee():
    print(f"Wheeee! {datetime.now().second}")

if __name__ == '__main__':
    say_whee()
