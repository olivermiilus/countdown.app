import time
from datetime import datetime

def countdown(target_date):
    while True:
        now = datetime.now()
        remaining_time = target_date - now

        if remaining_time.total_seconds() <= 0:
            print("Countdown finished!")
            break

        days, remainder = divmod(remaining_time.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Time remaining: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds", end='\r')
        time.sleep(1)

if __name__ == "__main__":
    # Specify the target date and time (year, month, day, hour, minute, second)
    target_date = datetime(2023, 12, 31, 23, 59, 59)
    countdown(target_date)