A = [5,4,3,-1,2,3]
A = [16, 17, 4, 3, 5, 2]
# create Right max array

def Solve(A):
    rght_max = [0] * len(A)
    rght_max[-1] = A[-1]
    for i in range(2, len(A)+1):
        rght_max[-i] = max(rght_max[-i+1], A[-i])
    return list(set(rght_max))


print("Right MAx array => ", Solve(A))