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
    # Prompt the user to enter the target date and time
    target_date_str = input("Enter the target date and time (YYYY-MM-DD HH:MM:SS): ")
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d %H:%M:%S")
    countdown(target_date)