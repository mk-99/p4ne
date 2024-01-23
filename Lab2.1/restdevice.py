import requests
import pprint

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

HOST = "https://10.31.70.209"
REST_OPER = "/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

r = requests.get(
    HOST + REST_OPER,
    verify=False,
    auth=("restapi", "j0sg1280-7@"),
    headers=headers,
)

if r.status_code == 200:
    device_data = r.json()
    pprint.pprint(device_data, width=30)
    print("===========")
    for current_int in device_data['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']:
        print("Interface: ", current_int['name'])
        print("Input packets/bytes: ", current_int['statistics']['in-unicast-pkts'], "/", current_int['statistics']['in-octets'])
        print("Output packets/bytes: ", current_int['statistics']['out-unicast-pkts'], "/", current_int['statistics']['out-octets'])

