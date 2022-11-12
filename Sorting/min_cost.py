A = [ 8, 9, 10 ]

def solve(A):
    A.sort(reverse=True)
    cost = 0
    for i in range(len(A)):
        cost += (i+1) * A[i]
    return cost

print(solve(A))