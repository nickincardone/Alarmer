import time
import sqlite3
import os

from datetime import datetime
from threading import Thread
from alarmer import LightSwitch

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..','db.sqlite')
conn = sqlite3.connect(filename)

def execute_query(query):
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    return c

def add(hour, minute, song='todo', weekdays='True'):
    execute_query("INSERT INTO alarms VALUES ('{}','{}','{}','{}')".format(hour, minute, song, weekdays))

def add_alarm(hour, minute, song='todo', weekdays='True'):
    execute_query("INSERT INTO alarms VALUES ('{}','{}','{}','{}')".format(hour, minute, song, weekdays))

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

def alarms():
    alarms = execute_query("SELECT * FROM alarms")
    resp = []
    for alarm in alarms:
        alarm_dict = {}
        alarm_dict['hour'] = int(alarm[0])
        alarm_dict['minute'] = int(alarm[1])
        alarm_dict['song'] = str(alarm[2])
        alarm_dict['weekdays'] = bool(alarm[3])
        resp.append(alarm_dict)
    return resp

def print_alarms():
    alarms = execute_query("SELECT * FROM alarms")
    for alarm in alarms:
        print(alarm)

def check_for_alarm():
    alarms = execute_query("SELECT * FROM alarms")
    for alarm in alarms:
        if alarm[3] == "true":
            if datetime.now().weekday() < 5 and datetime.now().hour == int(alarm[0]) and datetime.now().minute == int(alarm[1]):
                LightSwitch.on()
        else:
            if datetime.now().hour == int(alarm[0]) and datetime.now().minute == int(alarm[1]):
                LightSwitch.on()
    print(datetime.now())