import requests
from alarmer import config

url = "http://{ip}:49153/upnp/control/basicevent1".replace("{ip}", config.light_ip)
set_headers = {
    "Content-type": "text/xml",
    "SOAPACTION": '"urn:Belkin:service:basicevent:1#SetBinaryState"'
}
set_body = '<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"><BinaryState>{state}</BinaryState></u:SetBinaryState></s:Body></s:Envelope>'

get_headers = {
    "Content-type": "text/xml",
    "SOAPACTION": '"urn:Belkin:service:basicevent:1#GetBinaryState"'
}
get_body = '<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:GetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"><BinaryState>1</BinaryState></u:GetBinaryState></s:Body></s:Envelope>'

def on():
    r = requests.post(url, data=set_body.replace("{state}", "1"), headers=set_headers)

def off():
    r = requests.post(url, data=set_body.replace("{state}", "0"), headers=set_headers)

def get_status():
    r = requests.post(url, data=get_body, headers=get_headers)
    if r.status_code==200:
        i = r.text.find("</BinaryState>") - 1
        state = int(r.text[i:i+1])
        return 'on' if state == 1 else 'off'
    return "error"

