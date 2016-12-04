#!/usr/local/bin/python3

def numeric_ip(addr):
    """Converts string representation of IP address (i. e. 192.168.1.1) to integer"""
    num_ip, step = 0, 1
    for octet in reversed(addr.split('.')):
        num_ip += int(octet) * step
        step *= 2 ** 8
    return num_ip

def numeric_mask(mask):
    """Converts string representation of mask (i. e. /24) to integer"""
    return (0xffffffff << (32 - int(mask.lstrip('/')))) & 0xffffffff

class Subnet:
    def __init__(self, n="0.0.0.0", p="/0"):
        self.network = n
        self.prefix = p
    def __str__(self):
        return self.network + self.prefix
    def getnet(self):
        return self.network
    def getprefix(self):
        return self.prefix

class Ipaddr:
    def __init__(self, a="0.0.0.0"):
        self.addr = a
    def insubnet(self, subnet):
        return numeric_ip(subnet.getnet()) == (numeric_ip(self.addr) & numeric_mask(subnet.getprefix()))

class Addr_plan_entry(Subnet):
    def __init__(self, n="0.0.0.0", p="/0", gw="0.0.0.0"):
        Subnet.__init__(self, n, p)
        self.gateway = gw
    def getgw(self):
        return self.gateway


n1 = Subnet("192.168.1.0", "/24")
n2 = Subnet("172.16.0.0", "/16")
n3 = Subnet()

print(n1, n2, n3)
ip1 = Ipaddr("172.16.1.16")

print("%x" % ip1.insubnet(n1))
print("%x" % ip1.insubnet(n2))
print("%x" % ip1.insubnet(n3))

ap1 = Addr_plan_entry("192.168.1.0", "/24", "192.168.1.1")
print(ap1)
print(ap1.getgw())
