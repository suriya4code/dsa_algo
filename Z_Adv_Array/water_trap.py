A = [0, 1, 0, 2]

def solve(A):
    n = len(A)
    left = [0]*n
    right = [0]*n

    left[0] = A[0]
    for i in range(1,n):
        left[i] = max(left[i-1],A[i])
    
    right[n-1] = A[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1],A[i])

    water = 0
    for i in range(n):
        water += (min(left[i],right[i])-A[i])
    return water


solve(A)