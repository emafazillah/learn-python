'''
Created on 31 Dec 2018

@author: emafazillah
'''
N = int(raw_input())

if N % 2 == 0 and (N in range(2, 5) or N > 20):
    print("Not Weird")
else:
    print("Weird")
