import requests
import json
import pprint

url = 'https://sandboxapic.cisco.com/api/v1/ticket'
payload = {"username":"devnetuser","password":"Cisco123!"}
header = {"content-type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)

print(response.text)

pprint.pprint(response.json())
