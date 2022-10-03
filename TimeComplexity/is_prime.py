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
    count = 0
    root = int(math.sqrt(A))
    print(root)
    for i in range(1, root+1):
        if A%i == 0:
            count += 1
            if i*i != A:
                count += 1
    return True if count == 2 else False


print("IsPRIME => ",solve(1))

# class Solution:
#     # @param A : long
#     # @return an integer
#     def solve(self, A):
#         count = 0
#         root = int(math.sqrt(A))
#         for i in range(1, root+1):
#             if A%i == 0:
#                 count += 1
#                 if i*i != A:
#                     count += 1
#         return 1 if count == 2 else 0
