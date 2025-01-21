from flask import Flask, render_template, request
from datetime import datetime
import time
import threading

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])
        target_date = datetime(year, month, day, hour, minute)
        threading.Thread(target=countdown, args=(target_date,)).start()
        return f"Countdown started for {target_date}"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)