# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
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

# @calculate_time
# def Solve(A, B):
#     result = []
#     for i in B:
#         start, end = i[0],i[1]
#         sum_of = 0

#         for j in range(len(A)):
#             if j >= start-1 and   j <= end-1:
#                 sum_of += A[j]
#         result.append(sum_of)
#     return result

def sum_of_L_R(A, B):
    #prefix sum array
    ps = []
    ps.append(A[0])
    for j in range(1,len(A)):
        ps.append(A[j] + ps[j-1])
    result = []
    for i in B:
        start = i[0]-1
        end = i[1]-1
        if start in [0]:
            result.append((ps[end]))
        else:
            result.append((ps[end])-(ps[start-1]))
    return result
        


        
A = [1, 2, 3, 4, 5]
B = [[1, 4], [2, 3],[1,5]]

# A = [2, 2, 2]
# B = [[1, 1], [2, 3]]

print(sum_of_L_R(A, B))

# print(Solve(A, B))
# Starting time calculation
# Finished time calculation
# 0.04124641418457031
# [2, 4]