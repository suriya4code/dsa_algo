import math
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


A = [-3, 6, 2, 4, 5, 2, 8, -9, 3] * 999999
# A = [1,2,3]

@calculate_time
def brute_force(A):
    # T.C = O(n^2)
    # S.C = O(1)
    a_max = max(A)
    a_min = min(A)

    ans = math.inf
    for i in range(len(A)):
        if A[i] == a_min:
            for j in range(i + 1,len(A)):
                if A[j] == a_max:
                    ans = min(ans,j-i+1)
                    break
        
        elif A[i] == a_max:
            for j in range(i + 1,len(A)):
                if A[j] == a_min:
                    ans = min(ans,j-i+1)
                    break
    return ans

@calculate_time
def solve(A):
    a_max = max(A)
    a_min = min(A)

    min_index = -1
    max_index = -1
    ans = math.inf

    for i in range(len(A)):
        if A[i] == a_min:
            min_index = i
            if max_index != -1 and min_index != -1:
                ans = min(ans, abs(max_index-min_index)+1)
        elif A[i] == a_max:
            max_index = i
            if max_index != -1 and min_index != -1:
                ans = min(ans, abs(max_index-min_index)+1)        
       
    return ans


A = [ 377, 448, 173, 307, 108 ]
print("Brute Force => ", brute_force(A))
print("Solve  => ", solve(A))