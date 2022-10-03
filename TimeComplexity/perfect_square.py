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
def solve(A):
    root = int(math.sqrt(A))
    for i in range(1, root+1):
        if i*i == A:
            return 1
        if i*i > A:
            break
    return 0


print("IS Perfect Square => ",solve(10**10))
print("IS Perfect Square => ",solve(9))