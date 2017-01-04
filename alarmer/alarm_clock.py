import time
import sqlite3
import os

from datetime import datetime
from threading import Thread
from alarmer import light_switch

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..','db.sqlite')
conn = sqlite3.connect(filename)

def execute_query(query):
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    return c

def add_alarm(hour, minute, song='todo', weekdays):
    execute_query("insert into alarms values ('{}','{}','{}','{}')".format(hour, minute, song, weekdays))

def init():
    execute_query('''CREATE TABLE IF NOT EXISTS alarms
             (hour text, minute text, song text, weekdays text)''')

def run_schedule():
    while 1:
        check_for_alarm()
        time.sleep(60)

def run():
    t = Thread(target=run_schedule)
    t.start()

def check_for_alarm():
    #day of week where monday is 0
    if datetime.now().weekday() < 5 and datetime.now().hour == 20 and datetime.now().minute == 0:
        light_switch.off()
    if datetime.now().weekday() < 5 and datetime.now().hour == 8 and datetime.now().minute == 30:
        light_switch.off()
    print datetime.now()