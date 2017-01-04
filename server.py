from alarmer import AlarmClock
from flask import Flask

app = Flask(__name__)

@app.route("/api/alarms")
def get_alarms():
    return str(AlarmClock.alarms())

if __name__ == '__main__':
    AlarmClock.init()
    #AlarmClock.run()
    app.run()