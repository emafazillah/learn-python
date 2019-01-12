'''
Created on 31 Dec 2018

@author: emafazillah
'''
from __future__ import division

def integer_division(a, b):
    return a // b

def float_division(a, b):
    return a / b

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(integer_division(a, b))
    print(float_division(a, b))