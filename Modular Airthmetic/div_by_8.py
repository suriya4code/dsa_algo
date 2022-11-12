
A = "1000005"

print(A[-3:])

def solve(A):
    A = int(A)
    return 1 if A%8==0 else 0

print(solve(A))

