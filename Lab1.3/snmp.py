#!/usr/local/bin/python3

# Подключаем часть библиотеки 'pysnmp'. 'hlapi' означает high-level API
from pysnmp.hlapi import *

# Обрабатывать ошибки будем с помощью исключений. Определяем одно простейшее исключение "ошибка SNMP"
class Snmp_exception(Exception): pass

# Функция опроса по SNMP - принимает на вход объект-генератор, предоставленный библиотекой,
# проходит по нему, выводит результаты, при ошибках порождает исключения
def print_snmp(g):
    """Takes a generator object from pysnmp, prints snmp values"""
    # Actual request performs here.
    for snmp_result in g:
        errorIndication, errorStatus, errorIndex, varBinds = snmp_result
        if errorIndication:
            print(errorIndication)
            raise Snmp_exception
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            raise Snmp_exception
        else:
            for varBind in varBinds:
                print(varBind)
                print(' = '.join([x.prettyPrint() for x in varBind]))

try:
    # Библиотечная функция getCmd реализует SNMP-метод getcmd, возвращает объект-генератор,
    # при проходе по которому выполняются SNMP-запросы
    g = getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('10.31.70.107', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

    # Вывод результатов реализован как отдельная функция
    print_snmp(g)

    # Библиотечная функция nextCmd работает аналогично getCmd, но реализует SNMP-метод nextcmd
    n = nextCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('10.31.70.107', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
               lexicographicMode=False)

    print_snmp(n)
except:
    # Управление передаётся сюда из любых точек, где есть оператор raise
    print('Error - exception')
