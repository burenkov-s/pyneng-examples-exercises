# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from tabulate import tabulate

ips_reach = ['10.1.1.1', '10.1.1.2']
ips_unreach = ['10.1.1.7', '10.1.1.8', '10.1.1.9', '10.1.1.10']

def print_ip_table(ips_reach, ips_unreach):
    tabs = {'Reachable': ips_reach, 'Unreachable': ips_unreach}
    print(tabulate(tabs, headers='keys'))

if __name__=='__main__':
    print_ip_table(ips_reach, ips_unreach)