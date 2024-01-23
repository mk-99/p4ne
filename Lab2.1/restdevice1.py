import requests, json, pprint

host_ip = '10.31.70.210'
login = 'restapi'
password = 'j0sg1280-7@'

host_url = 'https://' + host_ip + ':55443'

r = requests.post(host_url + '/api/v1/auth/token-services', auth=(login, password), verify=False)
token = r.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get(host_url + '/api/v1/global/memory/processes', headers=header, verify=False)
ps_data = r.json()
pprint.pprint(sorted(ps_data['processes'], key=lambda x: x['memory-used'], reverse=True)[:10])
