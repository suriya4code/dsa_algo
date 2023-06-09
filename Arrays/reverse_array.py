from time import time
import math

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

@calculate_time
def solve(A):
    start = 0
    N = len(A)
    end = N-1

    while start < end:
        A[start],A[end] = A[end],A[start]
        start += 1
        end -= 1
        
    return A



print("Reversed Aay => ",solve(list(range(10))))