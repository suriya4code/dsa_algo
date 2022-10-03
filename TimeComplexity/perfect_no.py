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
    if A == 1:
        return 0
    sum_of_fact = 1
    root = int(math.sqrt(A))
    # print(root)
    for i in range(2, root+1):
        if A%i == 0:
            sum_of_fact = sum_of_fact + i + A/i
    return 1 if sum_of_fact == A else 0


print("IS Perfect Number => ",solve(10**10))
print("IS Perfect Number => ",solve(6))