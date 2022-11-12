A = [3,2,1,3]
A = [ -4, -2, 0, -1, -6 ]
A = [ -1, -2, 0, 0, 0, -3 ]

def solve(A):
    A.sort(reverse=True)
    for i in range(1,len(A)):
        if A[i] != A[i-1]:
            if abs(A[i]) == i:
                return 1
    return -1

print(solve(A))