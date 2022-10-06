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

def solve2(A, B):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] + A[j] == B and A[i] != A[j]:
                return 1
    return 0
# A : [ 1, 2, 3, 4 ]
# B : 7


print("Exisits pair => ",solve2([ 1, 2, 2 ],4))