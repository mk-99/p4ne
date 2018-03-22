#!/usr/local/bin/python3

# Подключаем библиотеки
from ipaddress import IPv4Network
import random

# Создаем класс, унаследованный от класса IPv4Network
class IPv4RandomNetwork(IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                              random.randint(p_start, p_end), False),
                             strict=False
                             )

    def regular(self):
        return self.is_global and not \
            (self.is_multicast or self.is_link_local or \
             self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)

    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)

# Служебная функция для передачи в качестве параметра в функцию sorted
def sortfunc(x):
    return x.key_value()

# Инициализируем генератор случайных чисел и список
random.seed()

rnlist = []

# Генерируем сети, помещаем в список
while len(rnlist) < 50:
    random_network = IPv4RandomNetwork(8, 24)
    if random_network.regular() and random_network not in rnlist: # проверка на регулярность и уникальность
        rnlist.append(random_network)

# И выводим на экран
for n in sorted(rnlist, key=sortfunc):
    print(n)
