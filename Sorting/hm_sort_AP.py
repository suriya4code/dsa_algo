A = [3, 5, 1]




def solve(A):
    n = len(A)
    A.sort()
    d = A[1]-A[0]
    for i in range(1,n-1):
        if A[i+1] - A[i] == d:
            continue
        else:
            return 0
    return 1



print(solve(A))