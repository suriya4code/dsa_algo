


import math


def solve(A, B):
    n = len(B)
    if n < 3:
        return -1
    minimum = float('inf')
    for i in range(1,n-1):
        left_min = float('inf')
        right_min = float('inf')
        for j in range(i):
            if A[j] < A[i] and B[j] < left_min:
                left_min = B[j]
        for j in range(i+1, n):
            if A[j] > A[i] and B[j] < right_min:
                right_min = B[j]
        minimum = min(minimum, left_min + B[i] + right_min)
    return -1 if minimum == float('inf') else minimum


A = [1, 3, 5]
B = [1, 2, 3]

A = [1, 6, 4, 2, 6, 9]
B = [2, 5, 7, 3, 2, 7]

def christ(A,B):
    N = len(A)
    if N < 3:
        return -1
    min_val = math.inf
    for i in range(1,N-1):
        left_min = math.inf
        right_min = math.inf
        for j in range(i):
            if A[j]< A[i] and B[j]<left_min:
                left_min = B[j]
        for k in range(i+1,N):
            if A[k]> A[i] and B[k]<right_min:
                right_min = B[k]
        min_val = min(min_val, (left_min+B[i]+ right_min))
    return -1 if min_val== math.inf else min_val


print(solve(A,B))
print(christ(A,B))