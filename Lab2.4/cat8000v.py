import requests

from flask import Flask, jsonify

# Credentials for test network device
net_device = "https://10.31.70.209"
login = 'restapi'
password = 'j0sg1280-7@'

def get_processes():

    headers = {
        "accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }

    r = requests.get(
        net_device + '/restconf/data/Cisco-IOS-XE-process-memory-oper:memory-usage-processes',
        headers=headers,
        auth=(login, password),
        verify=False,
    )
    if 200 <= r.status_code <= 299:
        return r.json()
    else:
        return None

app = Flask(__name__)

@app.route("/")
def index():
    ps_list = get_processes()
    ps_for_top_ten = [{
            'holding-memory': ps['holding-memory'],
            'name': ps['name']
        }
        for ps in ps_list['Cisco-IOS-XE-process-memory-oper:memory-usage-processes']['memory-usage-process']
    ]
    return jsonify(sorted(ps_for_top_ten, key=lambda x: int(x['holding-memory']), reverse=True)[0:10])

if __name__ == '__main__':
    app.run(debug=True)

