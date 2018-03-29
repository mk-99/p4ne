from flask import Flask, jsonify
import json
import sys
import re
import glob
import pprint

hosts = {}

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    s = """
        This server shows information about
        configs on /configs request and about 
        IP addresses on /config/<b>hostname</b> request"
    """
    return s

@app.route('/configs')
def host_info():
    r = []
    for h in hosts.keys():
        r.append(hosts[h]['name'])
    return jsonify(r)

@app.route('/config/<hostname>')
def ip_info(hostname):
    for h in hosts.keys():
        if hosts[h]['name'] == hostname:
            return jsonify(hosts[h]['addresses'])
    return jsonify("Not found")

if __name__ == '__main__':

    for current_file_name in glob.glob("/Users/mk/Seafile/p4ne_training/config_files/*.txt"):
        hosts[current_file_name] = {}
        hosts[current_file_name]['addresses'] = []

        with open(current_file_name) as f:
            for current_line in f:
                m = re.match("^hostname (.+)", current_line)
                if m:
                    hosts[current_file_name]['name'] = m.group(1)
                    continue
                m = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", current_line)
                if m:
                    hosts[current_file_name]['addresses'].append({'ip': m.group(1), 'mask': m.group(2)})


pprint.pprint(hosts)
app.run(debug=True)
