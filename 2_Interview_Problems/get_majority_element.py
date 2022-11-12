import math
from time import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        print("Starting time calculation")
        result = func(*args, **kwargs)
        print("Finished time calculation")
        end = time()
        print((end-start)*1000)
        return result
    return wrapper 


A = [3,4,3,6,1,3,2,3,3,1,3,3]
A = [ 1, 1, 1, 2, 3, 5, 7 ]

def solve(A):
    N = len(A)
    me = A[0]
    fq = 1

    for i in range(1, N):
        if A[i] == me:
            fq += 1
        else:
            if fq == 0:
                me = A[i]
                fq = 1
            else:
                fq -= 1
    if A.count(me) > N/2:
        return me
    else:
        return -1
        
print(solve(A))
