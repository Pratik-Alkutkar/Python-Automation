"""
Date:- 12-05-2024
Code No:- 5
Code:- Scheduling in Python - This program schedules after every 1 minute, 1 hour and after each Sunday.
"""

import datetime
import time
import schedule

def Schedule_Minute():
    print("Scheduler executes after each minute: ", datetime.datetime.now())

def Schedule_Hour():
    print("Scheduler executes after each hour: ", datetime.datetime.now())

def Schedule_Sunday():
    print("Scheduler executes after each Sunday: ", datetime.datetime.now())

def main():
    print("Current time is ", datetime.datetime.now())

    schedule.every(1).minutes.do(Schedule_Minute)
    schedule.every(1).hour.do(Schedule_Hour)
    schedule.every(1).sunday.do(Schedule_Sunday)

    while True:
        schedule.run_pending()
        time.sleep

if __name__ == "__main__":
    main()