# -*- coding: utf-8 -*-
"""
Source: https://www.youtube.com/watch?v=ZoWgzG_r2qo&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_
&index=4&ab_channel=sentdex
"""

''' Lists are faster, because a list is already loaded to your memory. Generators are slower
but do take less memory, because a generator is not loaded to your memory.

If you want to iterate through a list or a generator, the generator will take a longer time, 
because it is not loaded'''

#List comprehension, prints an actual list
xyz = [i for i in range(5)]
print(xyz)
# A generator, prints a generator object id
xyz = (i for i in range(5))
print(xyz)

for i in xyz:
    print (i)