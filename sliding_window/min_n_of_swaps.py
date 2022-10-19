import math


A = [19, 11, 3,9,7,25,6,20,4]
# A = [25,30,2,18,7,6,9,50,3]
A = [-2,-3, -4, -9, -6, -7, -8, -9, 10, -11]


def min_swaps(A,B):
    N = len(A)
    k = 0
    for i in A:
        if i <= B:
            k+=1
    if k == 0 or k == 1:
        return 0
    bc = 0
    ans = math.inf

    for i in range(k):
        if A[i] > B:
            bc+=1

    for s in range(1, N-k+1):
        e = k+s-1
        if A[e] > B:
            bc+=1
        if A[s-1] > B:
            bc-=1
        ans = min(bc,ans)
    return ans     

print(min_swaps(A,0))