#!/usr/local/bin/python3

from ipaddress import *
import random as r

class PrefixGenerator:
    def make(self, n=1):
        return [IPv4Network((r.randint(0x100, 0xE0000000), r.randint(1, 24)), strict=False) for i in range(0, n)]

r.seed()
g = PrefixGenerator()
for p in g.make():
    print(p)
