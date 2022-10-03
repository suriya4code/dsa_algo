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
    prime_count = 0
    for N in range(1,A+1):
        count = 0
        root = int(math.sqrt(N))
        for i in range(1, root+1):
            if N%i == 0:
                count += 1
                if i*i != N:
                    count += 1
        if count == 2:
            prime_count+=1
    return prime_count



print("IsPRIME => ",solve(13**3))