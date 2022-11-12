import math


A = 6
B = 12

def solve(A,B):
    min_a = math.inf
    min_b = math.inf
    for i in range(A):
        min_a = min(min_a, i ^ A)
    for j in range(B):
        min_b = min(min_b,j^B)
    return min_a + min_b

print(solve(A,B))