# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ospf = open('ospf.txt', 'r')
for line in ospf:
    tmp, prefix, metric, via, hop, update, intf = line.split()
    print("{:20} {:20}".format("Prefix", prefix))
    print("{:20} {:20}".format("AD/Metric", metric.strip('[]')))
    print("{:20} {:20}".format("Next-Hop", hop.strip(',')))
    print("{:20} {:20}".format("Last-update", update.strip(',')))
    print("{:20} {:20}".format("Outbound Interface", intf))
