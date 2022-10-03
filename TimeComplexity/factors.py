A = 10
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

@calculate_time
def factors_count(A):

    count = 0
    for i in range(1,A+1):
        if i*i==A:
            count += 1
            continue
        if i > A/i:
            return count
        if A%i == 0:
            count += 2
    
    return count


@calculate_time
def factor_while(A): #my solution passed
    i = 1
    count = 0
    while i*i <= A:
        if A%i == 0:
            if i*i == A:
                count += 1
            elif i>A/i:
                break
            elif A%i == 0:
                count += 2
        i+=1
    
    return count
import math
@calculate_time
def solve(A): #actual solution from scaler
    count = 0
    root = (int)(math.sqrt(A))
    for i in range(1 , root + 1):
        if A % i == 0:
            count += 1
            if i * i != A:
                count += 1
    return count


print("AAnswer",factor_while(10**11))
print("AAnswer",solve(10**11))


