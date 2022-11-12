import math


A = [1, 12, 10, 3, 14, 10, 5]
B = 8

def solve(A,B):
    k = 0
    for i in A:
        if i<=B: k +=1
    ans = math.inf
    for i in range(len(A)-k):
        c = 0
        for j in range(i,i+k):
            if A[j]<=B: c+=1
        ans = min(ans, k-c)
    return ans

print(solve(A,B))