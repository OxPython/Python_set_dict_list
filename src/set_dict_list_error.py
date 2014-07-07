'''
Created on Jul 7, 2014

@author: viejoemer

How to create a set with a dictionary in, in Python?

¿Cómo crear un set con un dict adentro, en Python?

'''

#Generating an error dict.
d = {'dict_key':'dict_value'}
s = set([d])

#Fix the problem but be careful.
f =  frozenset(d)
print(f)
f_keys = frozenset(d.keys())
print(f_keys)
f_values = frozenset(d.values())
print(f_values)

#Now you can create the set.
s = set([f])
print(s)

#Generating an error list.
l = ['list_value',1]
s = set([l])

#Fix the problem.
f =  frozenset(l)
print(f)

#Now you can create the set with list.
s = set([f])
print(s)