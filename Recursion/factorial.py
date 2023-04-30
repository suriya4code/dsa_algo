def solve(A):
    if A==1: return 1
    return solve(A-1) * A



print(solve(5))