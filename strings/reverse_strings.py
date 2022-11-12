def solve(self, A):
    n = len(A)
    ans = ""
    for i in range(n-1, -1, -1):
        ans += A[i]
    return ans