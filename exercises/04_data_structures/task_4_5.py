# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
#vlans1 = command1.split()
vlans1 = command1.split()[-1].split(',')
vlans2 = command2.split()[-1].split(',')
#vlans11 = vlans1[-1].split(',')
#vlans2 = command2.split()
#vlans22 = vlans2[-1].split(',')
set1 = set(vlans1)
set2 = set(vlans2)
result = list(set1 & set2)
#final_result = sorted(result)
#print(final_result)
print(sorted(result))
