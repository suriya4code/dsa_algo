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
    max_no = -math.inf
    for i in range(len(arr)):
        if (arr[i] > max_no):
            max_no = arr[i]
    no_of_max = arr.count(max_no)
    return len(arr)-no_of_max


print("no of elements => ",solve([-1,-2,-3,-1]))