import time
import sqlite3
import os

from datetime import datetime
from threading import Thread
from alarmer import LightSwitch

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..','db.sqlite')
conn = sqlite3.connect(filename)

def init():
    execute_query('''CREATE TABLE IF NOT EXISTS alarms
             (hour text, minute text, song text, weekdays text)''')

def execute_query(query):
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    return c

def add(data):
    hour = data['hour']
    minute = data['minute']
    song = str(data['song']) if 'song' in data else ''
    weekdays = str(data['weekdays']) if 'weekdays' in data and type(data['weekdays']) is bool else 'False'
    execute_query("INSERT INTO alarms VALUES ('{}','{}','{}','{}')".format(hour, minute, song, weekdays))

def delete(alarm_id):
    execute_query("DELETE FROM alarms where rowid={}".format(alarm_id))

def run_schedule():
    while 1:
        check_for_alarm()
        time.sleep(60)

def run():
    t = Thread(target=run_schedule)
    t.start()

def alarms():
    alarms = execute_query("SELECT rowid, * FROM alarms")
    resp = []
    for alarm in alarms:
        alarm_dict = {}
        alarm_dict['id'] = int(alarm[0])
        alarm_dict['hour'] = int(alarm[1])
        alarm_dict['minute'] = int(alarm[2])
        alarm_dict['song'] = str(alarm[3])
        alarm_dict['weekdays'] = True if alarm[4].upper()=='TRUE' else False
        resp.append(alarm_dict)
    return resp

def print_alarms():
    alarms = execute_query("SELECT rowid, * FROM alarms")
    for alarm in alarms:
        print(alarm)

def check_for_alarm():
    alarms = execute_query("SELECT rowid, * FROM alarms")
    for alarm in alarms:
        if alarm[3] == "true":
            if datetime.now().weekday() < 5 and datetime.now().hour == int(alarm[0]) and datetime.now().minute == int(alarm[1]):
                LightSwitch.on()
        else:
            if datetime.now().hour == int(alarm[0]) and datetime.now().minute == int(alarm[1]):
                LightSwitch.on()
    print(datetime.now())