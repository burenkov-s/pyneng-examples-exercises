# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_is_correct = False
while True:
    ip_is_correct = True
    ip = input("Введите IP адрес:")
    octets = ip.split(".")
    if len(octets) == 4:
        for octet in octets:
            if int(octet) < 0 or int(octet) > 255:
                ip_is_correct = False
                break
    else:
        ip_is_correct = False
    if ip_is_correct:
        break
    else:
        print("IP is not correct. Try again")

if ip_is_correct:
    if int(ip.split(".")[0]) in range(1, 223):
        print("unicast")
    elif int(ip.split(".")[0]) in range(224, 239):
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
else:
    print("ip is not correct")