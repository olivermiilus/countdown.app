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
        target_date_str = request.form['target_date']
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d %H:%M:%S")
        threading.Thread(target=countdown, args=(target_date,)).start()
        return f"Countdown started for {target_date_str}"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)