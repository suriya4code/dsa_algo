# You are given an array A of length N and Q queries given by the 2D array B of size Q*2. Each query consists of two integers B[i][0] and B[i][1].
# For every query, the task is to calculate the sum of all even indices in the range A[B[i][0]…B[i][1]].

# Note : Use 0-based indexing

A = [1, 2, 3, 4, 5]
B = [[0,2], [1,4]]

def solve(A,B):
    N = len(A)
    res = []
    pse = []
    pse.append(A[0])
    for i in range(1,N):
        if i % 2 != 0:
            pse.append(pse[i-1])
        else:
            pse.append(pse[i-1]+A[i])
    for j in B:
        s = j[0]
        e = j[1]
        if s == 0:
            sum_of = pse[e]
        else:
            sum_of = pse[e]-pse[s-1]
        res.append(sum_of)
    return res


print(solve(A,B))