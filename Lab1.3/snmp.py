#!/usr/local/bin/python3

# Import some objects from 'pysnmp' library. 'hlapi' means high-level API
from pysnmp.hlapi import *

def print_snmp(g):
    """Takes a generator object from pysnmp, prints snmp values"""
    # Actual request performs here.
    for snmp_result in g:
        errorIndication, errorStatus, errorIndex, varBinds = snmp_result
        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))

# g is a 'generator' object, it's elements returned are lists of [errorIndication, errorStatus, errorIndex, varBinds]
g = getCmd(SnmpEngine(),
           CommunityData('public', mpModel=0),
           UdpTransportTarget(('10.31.70.107', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

# Now it is time to print results
print_snmp(g)

n = nextCmd(SnmpEngine(),
           CommunityData('public', mpModel=0),
           UdpTransportTarget(('10.31.70.107', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
           lexicographicMode=False)

print_snmp(n)