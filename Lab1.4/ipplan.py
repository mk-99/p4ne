#!/usr/local/bin/python3

from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                              random.randint(p_start, p_end), False),
                             strict=False
                             )
    def key_value(self):
        return int(self.network_address._ip) + (int(self.netmask._ip) << 32)

def sortfunc(x):
    return x.key_value()

random.seed()

rnlist = []

for i in range(0, 50):
    rnlist.append(IPv4RandomNetwork(8, 24))

for n in sorted(rnlist, key=sortfunc):
    print(n)
