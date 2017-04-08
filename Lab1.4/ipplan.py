#!/usr/local/bin/python3

from ipaddress import *
import random as r

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        IPv4Network.__init__(self, (r.randint(0x100, 0xE0000000), r.randint(p_start, p_end), False), strict=False)
    def keyfunc(self):
        return int(self.network_address._ip) + (int(self.netmask._ip) << 32)

r.seed()

rnlist = []

for i in range(0, 50):
    rnlist.append(IPv4RandomNetwork(8, 24))

for n in sorted(rnlist, key=lambda x: x.keyfunc()):
    print(n)
