# -*- coding: utf-8 -*-
"""
Source:https://www.youtube.com/watch?v=bMxEU0iG-KA&list=
PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=8&ab_channel=sentdex
"""

x = [1, 2, 3, 4]
y = [6, 7, 8, 9]
z = ['a', 'b', 'c', 'd']

# Zip function takes elements from multiple iterables and aggregates into one data
# structure where they share same index value
for a,b in zip(x,y):
    print(a,b)

# This prints a zip object
print(zip(x,y,z))

for i in zip(x,y,z):
    print(i)
    
# print a dictionary using two lists
print(dict(zip(x, y)))

# in regular loops values are stored in variables, but not in list comprehensions