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


def reverse(arr,i,j):
    start = i
    end = j

    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
        
    return arr

# A = [ 8, 7, 7, 6, 6, 3, 1, 5, 7 ]
# B = 0
# C = 3
# print("Reversed array from B to C=> ",reverse(A,B,C))



@calculate_time
def solve(arr,N,k):
    k = N%k
    r1 = reverse(arr,0,N-1)
    r2 = reverse(r1,0,k-1)
    r3 = reverse(r2,k,N-1)

    return r3
    




print("Reversed array => ",solve(list(range(10)),10,13))