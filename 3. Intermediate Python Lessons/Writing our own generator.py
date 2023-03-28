# -*- coding: utf-8 -*-
"""
Source:https://www.youtube.com/
watch?v=PewCyZSrnOI&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=9&ab_channel=sentdex
"""
# Generators do not return things, Generators yield things
def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'
    
for i in simple_gen():
    print(i)
    
correct_combo = (3, 6, 1)

for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print('Found the combo: {}' .format((c1, c2, c3)))
            print(c1, c2, c3)
            
# To run the code above to stop when the combination is found, need lot of code
correct_combo = (3, 6, 1)

found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print('Found the combo: {}' .format((c1, c2, c3)))
                found_combo = True
                break
            print(c1, c2, c3)
            
            
            
            
correct_combo = (3, 6, 1)
# Rather than using for loops, we can use a generator
# This is not saving a lot of lines, but easy to understand and saves memory
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1, c2, c3)
                
for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == correct_combo:
        print('Found the combo: {}' .format((c1, c2, c3)))
        break
    print(c1, c2, c3)










