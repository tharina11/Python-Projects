# Define a function to divide a number by another number

def divide(x, y):
    return x / y

#divide(6, 2)

''' The function above will throw an error when the denominator is 
zero. This is where a decorator is helpful. below is a simple example 
of a decorator'''

def check(function):
    '''Checks if the denominator is zero. If zero, print the error.
       If not, perform the division and return the result'''
    def inside(x, y):
        if y ==0:
            print("Result is undefined")
            return 
        function(x,y)
    return inside
        
#divide = check(divide)
#print(divide(6, 0))

'''This is a common pattern in Python. Therefore Python adds a decorator to 
handle the repititive pattern in Python codes'''

@check
def divide(x, y):
    return x / y

divide(6, 2)

'''Reference: https://www.youtube.com/watch?v=MYAEv3JoenI&ab_channel=howCode
              https://www.youtube.com/watch?v=yNzxXZfkLUA&ab_channel=Telusko'''

def div(a, b):
    print(a/b)
    
def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    
    return inner

div = smart_div(div)

div(4,2)