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
def solve(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i + j == k:
                return True
    return False



print("Exisits pair => ",solve(list(range(10**6)), 10**4))