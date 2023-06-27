# -*- coding: utf-8 -*-
"""
Source: https://www.youtube.com/watch?v=bOGmYvtw-kk&list=
PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=7&ab_channel=sentdex
"""

example = ['left', 'right', 'up', 'down']


# We get the same output in both codes below
for i in range(len(example)):
    print(i, example[i])
    
for i,j in enumerate(example):
    print(i, j)

# Create a new dictionary using enumerate
new_dict = dict(enumerate(example))
print(new_dict)