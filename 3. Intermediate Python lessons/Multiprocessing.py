# -*- coding: utf-8 -*-
"""
Source:https://www.youtube.com/watch?v=oEYDqQ1pq9o&list=
PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=10&ab_channel=sentdex 
"""
# Multi processing allows us to utilize multiple processors, multi processing
# libraries launch separate python processes

import multiprocessing

def spawn(num):
    print("spawned! {}".format(num))

# The below row is necessary in multiprocessing
# If this script is called by itself, it will run
# If this script is called by something else, it won't run    
if __name__ == '__main__':
    for i in range(50):
        p= multiprocessing.Process(target=spawn, args= (i,))
        p.start()
        #p.join()
        

