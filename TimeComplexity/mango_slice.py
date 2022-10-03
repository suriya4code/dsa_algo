#A = Mango
#B = Slice
'''
Given two integers A and B. A represents the count of mangoes and
 B represent the count of slices of mangoes. Mango can be cut into three slices of mangoes. 
 A glass of mango shake can be formed by two slices of mangoes.

Find the maximum number of glasses of mango shakes you can make with A mangoes and B slices of mangoes initially.
'''

from time import time
import math

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        print("Starting time calculation")
        result = func(*args, **kwargs)
        print("Finished time calculation")
        end = time()
        print("Time taken => ",(end-start)*1000)
        return result
    return wrapper

@calculate_time
def solve(A,B):
    return int((3*A + B)/2)


print("IS Perfect Square => ",solve(19,0))
print("IS Perfect Square => ",solve(7,1))