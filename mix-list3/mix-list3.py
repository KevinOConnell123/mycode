#!/usr/bin/env python3
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)
list1.extend(['juniper'])
print(list1)
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)
print(list1[4])
print(list1[4][0])
list2 = [ 'ant', 'bee', 'dog', 'cat', 'doe']
print(list2)
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[4])
print(list2[0:5])
a = ["ant", "bee", "dog"]
print(' '. join(a))

