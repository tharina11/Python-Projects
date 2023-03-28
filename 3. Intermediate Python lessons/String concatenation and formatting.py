# -*- coding: utf-8 -*-
"""
Source: https://www.youtube.com/watch?v=jA5LW3bR0Us&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_
&index=2&ab_channel=sentdex
"""

names = ['Jeff', 'Gary', 'Jill', 'Samantha']

#for name in names:
#    #print('Hello there, ' + name)
#    print(' '.join(['Hello there,',  name]))
    
# When you need to print the names as a list of strings, this has less processing
print(', '.join(names))



# This is not the optimum awy to go in terms of processing speed
location_of_files = 'C:\\Users\\H\\Desktop'
file_name = 'example.txt'
print(location_of_files+'\\' + file_name)

# Correct way is, this is convenient to use with multiple file path variables
import os

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read)
    
# String formatting
who = 'Gary'
how_many = 12

# Let's print 'Gary bought 12 apples today!

# This is not the best way to print the result
print(who,'bought',how_many,'apples today!')

# best way to write is 
print('{} bought {} apples today!'.format(who, how_many))
