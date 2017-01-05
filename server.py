from alarmer import AlarmClock, LightSwitch
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/api/alarms", methods=['POST', 'GET'])
def get_alarms():
    if request.method == 'GET':
        return str(AlarmClock.alarms())
    else:
        print(request.get_json(force=True))
        return 'bal'
        #return AlarmClock.create_alarm(request.get_json(force=True))

@app.route("/api/light/on", methods=['GET'])
def turn_on_light():
    LightSwitch.on()
    return json.dumps({'status': LightSwitch.status()})

@app.route("/api/light/off", methods=['GET'])
def turn_off_light():
    LightSwitch.off()
    return json.dumps({'status': LightSwitch.status()})

@app.route("/api/light/status", methods=['GET'])
def light_status():
    return json.dumps({'status': LightSwitch.status()})

if __name__ == '__main__':
    AlarmClock.init()
    #AlarmClock.run()
    app.run()