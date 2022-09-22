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
        if i > A/i:
            return count
        if A%i == 0:
            count += 2
    
    return count

print("AAnswer",factors_count(20**10))


