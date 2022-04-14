# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    result = list()
    access = dict()
    trunk = dict()
    with open(config_filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("interface FastEthernet"):
                interface = line.replace("interface ", "")
            if line.startswith("switchport access"):
                vlan = int(line.split()[-1])
                access[interface] = vlan
            elif line.startswith("switchport mode access"):
                vlan = 1
                access[interface] = vlan
            elif line.startswith("switchport trunk allowed"):
                vlan = line.split()[-1].split(',')
                trunk[interface] = list(int(x) for x in vlan)
    result.append(access)
    result.append(trunk)
    return tuple(result)


print(get_int_vlan_map('config_sw2.txt'))
