# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите айпи адрес и маску сети:")
print("Network:")
ip, netmask = ip.split("/")
ip = ip.split(".")
oct0, oct1, oct2, oct3 = [int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])]
print("{:<8} {:<8} {:<8} {:<8}".format(oct0, oct1, oct2, oct3))
print("{:08b} {:08b} {:08b} {:08b}".format(oct0, oct1, oct2, oct3))
print("Mask:")
netmask = "1" * int(netmask) + "0" * (32 - int(netmask))
m0, m1, m2, m3 = [netmask[0:8], netmask[8:16], netmask[16:24], netmask[24:32]]
print("{:<8} {:<8} {:<8} {:<8}".format(int(m0, 2), int(m1, 2), int(m2, 2), int(m3, 2)))
print("{:<08} {:<08} {:<08} {:<08}".format(int(m0), int(m1), int(m2), int(m3)))
