#!/usr/local/bin/python3

# Import some objects from library
from pysnmp.hlapi import *

# Initialize accessory objects

engine = SnmpEngine()
community_data = CommunityData('public')
transfer_method = UdpTransportTarget(('10.31.70.107', 161))
mib_object = ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))

g = getCmd(engine, community_data, transfer_method, ContextData(), mib_object) # g is a 'generator'

errorIndication, errorStatus, errorIndex, varBinds = next(g) # Actual request performs here. Multiple assignment example

for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))

mib_object = ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
