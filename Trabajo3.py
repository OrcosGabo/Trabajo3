import requests
import urllib3
import json
import conf

urllib3.disable_warnings()
url="https://192.168.100.215"

r = requests.post(url+"/rest/tool/bandwidth-test", auth=(conf.user,conf.clave), verify=False)
print(json.dumps(r.json(), indent=2))

