from ciscoconfparse import CiscoConfParse

parser = CiscoConfParse("cisco.cfg", syntax="ios")

# Находим все интерфейсы
all_interfaces = parser.find_objects(r'^interface')
for intf in all_interfaces:
    print(intf.text)
    # Находим IP-адрес
    ip_addr = intf.re_match_iter_typed(r'ip address (.+?) (.+)', default="")
    print(ip_addr)
