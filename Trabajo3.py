import requests
import urllib3
import json
import conf

urllib3.disable_warnings()
url="https://192.168.100.215"

r = requests.get(url+"/rest/ip/address/*3", auth=(conf.user,conf.clave), verify=False)
#print(json.dumps(r.json(), indent=2))

r2 = requests.get(url + "/rest/interface/ether1", auth=(conf.user,conf.clave), verify=False)
#print(r2.json()["mac-address"])

if r2.json()["mac-address"] == "00:0C:29:10:C7:72":
    print("El equipo no fue cambiado")
else:
    print("Alguien cambio el equipo!!!")