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
def solve(arr):
    start = 0
    N = len(arr)
    end = N-1

    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
        
    return arr



print("Reversed array => ",solve(list(range(10))))