'''
Created on 31 Dec 2018

@author: emafazillah
'''
def a_sum_b(a, b):
    return a + b

def a_minus_b(a, b):
    return a - b

def a_multiply_b(a, b):
    return a * b

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a_sum_b(a, b))
    print(a_minus_b(a, b))
    print(a_multiply_b(a, b))
    