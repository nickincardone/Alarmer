from alarmer import AlarmClock, LightSwitch
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/api/alarms", methods=['POST', 'GET'])
def get_alarms():
    if request.method == 'GET':
        return str(AlarmClock.alarms())
    else:
        data = request.get_json(force=True)
        if 'hour' in data and 'minute' in data:
            AlarmClock.add(data)
            return str(AlarmClock.alarms())
        else:
            return '{"error": "Hour and Minute required"}'

@app.route("/api/alarms/<int:alarm_id>", methods=['DELETE'])
def delete_alarm(alarm_id):
    AlarmClock.delete(alarm_id)
    return str(AlarmClock.alarms())

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