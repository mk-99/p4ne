#!/usr/local/bin/python3

from ipaddress import *

class IPv4AddrPlanEntry(IPv4Network):
    def __init__(self):


if __name__ == '__main__':
    ipplan1 = IPv4AddrPlanEntry(ip_network('192.168.1.0/24'))
    print(ipplan1)