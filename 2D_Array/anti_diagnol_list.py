# Give a N * N square matrix A, return an array of its anti-diagonals. 
# Look at the example for more details.

A = [[1,2,3,4],[5,6,7,8],[9,2,3,4], [5,6,7,8]]
A = [[1,2,3],[4,5,6],[7,8,9]]


def diagnol_sum(A):
    rows = col = len(A)
    result = []
    for c in range(col):
        a = []
        r = 0
        while r < rows and c >= 0:
            a.append(A[r][c])
            r += 1
            c -= 1
        while len(a)<rows:
            a.append(0)
        result.append(a)
    for r in range(1,rows):
        a = []
        c = col-1
        while r < rows and c >= 0:
            a.append(A[r][c])
            r += 1
            c -= 1
        while len(a)<rows:
            a.append(0)
        result.append(a)
    return result


def diagnol_sum_sln(A):
    p = len(A[0])
    res = [0]*(2*p-1)
    for i in range((2*p)-1):
        res[i] = []
    for i in range(p):
        for j in range(p):
            res[i+j].append(A[i][j])
    for i in range(2*p-1):
        while len(res[i]) < p:
            res[i].append(0)
    return res

print(diagnol_sum(A))
print(diagnol_sum_sln(A))