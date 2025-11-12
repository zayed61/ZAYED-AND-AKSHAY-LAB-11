"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
<<<<<<< HEAD

import math
def add(a, b): 
    return a + b
def sub(a, b):
=======
import math

def add(a, b): 

    return a + b
def sub(a, b):

>>>>>>> f03e68e74c510b96eb524453ed9660a7ee9222ea
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
<<<<<<< HEAD
        raise ZeroDivisionError
    else:
        return b/a
def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        return math.log(b, a)
def exp(a, b):
    return a ** b
=======
        return ZeroDivisionError
    else:
        return b / a

def log(a,b):
    if a<=0 or b<=0:
        raise ValueError
    else:
        return math.log(b,a)

def exp(a,b):
    return a**b


>>>>>>> f03e68e74c510b96eb524453ed9660a7ee9222ea
