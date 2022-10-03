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
def Solve(A):
    is_square_num = -1
    for i in range(1,A+1):
        if i*i == A:
            is_square_num=i
        if i*i > A:
            break
    return is_square_num


print("Is Square num => ",Solve(10**12))