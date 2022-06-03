import requests, json, pprint, ssl

from flask import Flask, render_template, jsonify
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

# Credentials for test network device
net_device = "https://10.31.70.210:55443"
login = 'restapi'
password = 'j0sg1280-7@'

class Ssl1HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
net_session = requests.Session()
net_session.mount(net_device, Ssl1HttpAdapter())

def new_token():
    r = net_session.post(net_device + '/api/v1/auth/token-services', auth=(login, password), verify=False)
    if 200 <= r.status_code <= 299:
        return r.json()["token-id"]
    else:
        return None

def get_processes(token):
    header = {
        "content-type": "application/json",
        "X-Auth-Token": token
    }
    r = net_session.get(net_device + '/api/v1/global/memory/processes', headers=header, verify=False)
    if 200 <= r.status_code <= 299:
        return r.json()
    else:
        return None

app = Flask(__name__)

@app.route("/")
def index():
    L = sorted(get_processes(t)['processes'], key=lambda x: x["memory-used"], reverse=True)[0:10]
    return jsonify(L)

if __name__ == '__main__':

    t = new_token()
    app.run(debug=True)

