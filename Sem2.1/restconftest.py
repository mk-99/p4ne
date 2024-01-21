import requests
import pprint

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

HOST = "https://10.31.70.209"
RES1 = "/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet/1"
RES2 = "/restconf/data/Cisco-IOS-XE-interfaces-oper:native/interface/GigabitEthernet/1"


r = requests.get(
    HOST + RES2,
    verify=False,
    auth=("jet", "q1q1q1"),
    headers=headers,
)
print(r.status_code)
pprint.pprint(r.json())

