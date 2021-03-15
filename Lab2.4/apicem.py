import requests, json, pprint

from flask import Flask
from flask import render_template, jsonify


# controller = "devnetapi.cisco.com/sandbox/apic_em"

controller = "sandboxapicem.cisco.com"

def new_ticket():
    url = 'https://' + controller + '/api/v1/ticket'
    payload = {"username": "devnetuser",
               "password": "Cisco123!"
              }
    header = {"content-type": "application/json"}

    response = requests.post(url, data=json.dumps(payload),
                             headers=header, verify=False)

    return response.json()['response']['serviceTicket']


def get_hosts(ticket):
    url = "https://" + controller + "/api/v1/host"

    header = {"content-type": "application/json",
              "X-Auth-Token":ticket
             }

    response = requests.get(url, headers=header, verify=False)

    return response.json()


def get_devices(ticket):
    url = "https://" + controller + "/api/v1/network-device"

    header = {"content-type": "application/json",
              "X-Auth-Token": ticket
              }

    response = requests.get(url, headers=header, verify=False)

    return response.json()

def get_topo(ticket):
    url = "https://" + controller + "/api/v1/topology/physical-topology"

    header = {"content-type": "application/json",
              "X-Auth-Token": ticket
              }

    response = requests.get(url, headers=header, verify=False)

    return response.json()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("topology.html")

@app.route("/api/topology")
def topology():
    ticket = new_ticket()
    return jsonify(get_topo(ticket)['response'])

if __name__ == '__main__':

    ticket = new_ticket()


    print("Hosts = ")
    pprint.pprint(get_hosts(ticket))

    print("Devices = ")
    pprint.pprint(get_devices(ticket))

    print("Topology = ")
    pprint.pprint(get_topo(ticket))

    app.run(debug=True)

