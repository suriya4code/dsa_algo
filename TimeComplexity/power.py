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
def Solve(A,B):
    if A==1:
        return 1
    else:
        return A**B


print("A Power B is => ",Solve(1000,120))