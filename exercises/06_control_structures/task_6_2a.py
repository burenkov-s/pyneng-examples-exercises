# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP адрес:")
ip_is_correct = False
octets = ip.split(".")
if len(octets) == 4:
    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            ip_is_correct = False
            break
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