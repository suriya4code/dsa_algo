A = [3, 4, -1, 1]
# A = [-8, -7, -6]
# A = [ 2, 3, 1, 2 ]

def solve(A):
    n = len(A)
    i = 0
    while i < n:
        if A[i]>0 and A[i]<n+1:
            if A[i] != i+1:
                pos = A[i]-1
                if A[pos] != A[i]:
                    A[i], A[pos] = A[pos], A[i]
                    i-=1
        i+=1
    for i in range(n):
        if A[i] != i+1:
            return i+1
    return n+1


print(solve(A))