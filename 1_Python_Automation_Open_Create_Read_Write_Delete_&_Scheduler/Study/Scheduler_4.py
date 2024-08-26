"""
Date:- 12-05-2024
Code No:- 4
Code:- Scheduling in Python - This program gives current time and gives time after every 1 minute.
"""

import datetime
import time
import schedule

def Schedule_Minute():
    print("Scheduler executes after each minute: ", datetime.datetime.now())


def main():
    print("Current time is ", datetime.datetime.now())

    schedule.every(1).minutes.do(Schedule_Minute)

    while True:
        schedule.run_pending()
        time.sleep

if __name__ == "__main__":
    main()