# Given an array of integers A, of size N.

# Return the maximum size subarray of A having only non-negative elements.
#  If there are more than one such subarray, return the one having the smallest starting index in A.

# NOTE: It is guaranteed that an answer always exists.

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


A = [5, 6, -1, 7, 8]
# A = [1, 2, 3, 4, 5, 6]
A = [ 8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ]
# A = [ -4549634, -3196682, 8455838, -1432628, -263819, -3928366, -5556259, -2114783, 3923939, -4183708 ]
# A : [ 8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ]

@calculate_time
def min_index_subArray(A):
    count = 0
    N = len(A)
    res = 0
    min_index = math.inf
    max_size = 0
    for i in range(N):
        if A[i] < 0:
            a= []
            ind =0
            for s in range(i,0,-1):
                if A[s-1]>0:
                    a.insert(0,A[s-1])
                else:
                    ind = s-1
                    break
            if len(a) > max_size:
                res = a
                max_size = len(a)
                min_index = ind
            elif len(a) == max_size:
                if ind <= min_index:
                    min_index = ind
                    res = a
            
            b=[]
            ind_b = N
            for e in range(i+1,N):
                if A[e]>0:
                    b.append(A[e])
                else:
                    ind_b = e-1
                    break
            if len(b)> max_size:
                res = b
                max_size = len(b)
                min_index = ind_b   
            elif len(b) == max_size:
                if ind_b <= min_index:
                    min_index = ind_b
                    res = b

        else:
            count += 1
    if count == N: return A
    return res

@calculate_time
def solve(A):
    ret = [[]]
    for i in A:
        if i < 0:
            ret.append([])
        else:
            ret[-1].append(i)
    mxlen = max([len(i) for i in ret])
    for i in ret:
        if len(i) == mxlen:
            return i    

    


print(min_index_subArray(A))            
print(solve(A))            
        
    


    