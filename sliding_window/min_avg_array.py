import math


A=[3, 7, 90, 20, 10, 50, 40]
B=3

A=[3, 7, 5, 20, -10, 0, 12]
B=2

def solve(A, B):
    N=len(A)
    sum_of = 0
    avg = math.inf
    min_i = 0

    for i in range(B):
        sum_of += A[i]

    avg = sum_of / B

    for i in range(B,N):
        s = i-B
        sum_of = sum_of + A[i] - A[s]
        if (sum_of/B) < avg:
            min_i = i-B+1
            avg = sum_of/B
    return min_i

print(solve(A,B))   
