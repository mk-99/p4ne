import requests
import pprint

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

HOST = "https://10.31.70.209"
REST_HOSTNAME = "/restconf/data/Cisco-IOS-XE-native:native/hostname"
REST_INTERFACE = "/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet/1"
REST_INTERFACE_2 = "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"
REST_OPER = "/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

r = requests.get(
    HOST + REST_OPER,
    verify=False,
    auth=("restapi", "j0sg1280-7@"),
    headers=headers,
)
print(r.status_code)
pprint.pprint(r.json(), width=30)

