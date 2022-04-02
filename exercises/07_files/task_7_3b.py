# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan_input = input("Enter VLAN number: ")

result = list()

with open('CAM_table.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            if line[0].isdigit():
                words = line.split()
                if words[0] == vlan_input:
                    words[0] = int(words[0])
                    result.append(words)
    result.sort()
    for line in result:
        vlan, mac, type, interface = line
        print("{:<7} {:17} {:7}".format(vlan, mac, interface))

