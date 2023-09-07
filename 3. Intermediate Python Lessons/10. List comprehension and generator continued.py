# -*- coding: utf-8 -*-
"""
Source: https://www.youtube.com/watch?v=MJUbUDa-YCA&ab_channel=sentdex
"""
input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

# This returns a list
[print(i) for i in xyz]

# This does not return anything because this is a generator
(print(i) for i in xyz)

[[print(i,ii) for ii in range(5)] for i in range(5)]

xyz = [[(i,ii) for ii in range(5)] for i in range(5)]
print(xyz)

xyz = ([(i,ii) for ii in range(5)] for i in range(5))
print(xyz)

for i in xyz:
    for ii in i:
        print(ii)
        
""" With big list comprehesions you will run out of memory. With big generators you
will run out of time"""