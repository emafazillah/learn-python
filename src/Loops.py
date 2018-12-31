'''
Created on 31 Dec 2018

@author: emafazillah
'''
def power_of(n):
    return n * n

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0, n):
        print(power_of(i))