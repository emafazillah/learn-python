'''
Created on 31 Dec 2018

@author: emafazillah
'''
def is_leap(year):
    leap = False
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(raw_input())
print is_leap(year)