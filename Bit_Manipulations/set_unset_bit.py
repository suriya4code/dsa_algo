A = 49
B = 0

def solve(A, B):
    if (A>>B) & 1 != 0:
        return A ^ (1<<B)
    return A

print(solve(A,B))