#l# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

'''
split_ospf_route = ospf_route.split()
d_keys = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
vocab = dict.fromkeys(d_keys)
vocab['Prefix'] = split_ospf_route[0]
vocab['AD/Metric'] = split_ospf_route[1]
vocab['Next-Hop'] = split_ospf_route[3]
vocab['Last update'] = split_ospf_route[4]
vocab['Outbound Interface'] = split_ospf_route[5]
d_values = dict.values(vocab)
string_values = ','.join(d_values)
string_keys = ','.join(d_keys)
ip_template = 
    ...: IP address: {} 
    ...:  
print(ip_template.format(string_values[0:12]))
#print(vocab)
#for v,d in vocab.items():
#    print("{:<15} {:<15}".format(v,d))
'''

list1 = ospf_route.split()
list1.pop(2)
list1[1] = '110/41'
list1[2] = '10.0.13.3'
list1[3] = '3d18h'
d_keys = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
tuple_keys = tuple(d_keys)
vocab = { 
         (tuple_keys[0]):(list1[0]),
         (tuple_keys[1]):(list1[1]),
         (tuple_keys[2]):(list1[2]),
         (tuple_keys[3]):(list1[3]),
         (tuple_keys[4]):(list1[4]),
         } 

print("{:20} {:20}".format(tuple_keys[0], vocab.get('Prefix')))
print("{:20} {:20}".format(tuple_keys[1], vocab.get('AD/Metric')))
print("{:20} {:20}".format(tuple_keys[2], vocab.get('Next-Hop')))
print("{:20} {:20}".format(tuple_keys[3], vocab.get('Last update')))
print("{:20} {:20}".format(tuple_keys[4], vocab.get('Outbound Interface')))

