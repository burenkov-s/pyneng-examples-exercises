# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from ipaddress import ip_address
import subprocess

ipaddresses = ["127.0.0.1", "192.168.1.1", "8.8.8.8", "10.10.10.10"]
def ping_ip_addresses(ipaddresses):
    reach = []
    unreach = []
    for address in ipaddresses:
        ip = ip_address(address)
        if subprocess.run('ping -c 1 -n ' + str(ip), shell=True).returncode == 0:
            reach.append(str(ip))
        else:
            unreach.append(str(ip))
    return (reach, unreach)

if __name__=="__main__":
    print(ping_ip_addresses(ipaddresses))
