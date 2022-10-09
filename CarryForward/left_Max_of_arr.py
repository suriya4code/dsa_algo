A = [-3, 6, 2, 4, 5, 2, 8, -9, 3]

# create left max array

def Solve(A):
    lft_max = [0] * len(A)
    lft_max[0] = A[0]
    for i in range(0, len(A)):
        lft_max[i] = max(lft_max[i-1], A[i])
    return lft_max

print("Left MAx array => ", Solve(A))