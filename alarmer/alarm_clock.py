from datetime import datetime
from threading import Thread
import time
from alarmer import light_switch

def run_schedule():
    while 1:
        check()
        time.sleep(60)

def run():
    t = Thread(target=run_schedule)
    t.start()

def check():
    #day of week where monday is 0
    if datetime.now().weekday() < 5 and datetime.now().hour == 20 and datetime.now().minute == 0:
        print "yasss"
        light_switch.off()
        return True
    if datetime.now().weekday() < 5 and datetime.now().hour == 8 and datetime.now().minute == 30:
        print "yasss"
        light_switch.off()
        return True
    print datetime.now()
    return False