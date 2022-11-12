A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]


def solve(A,B):
        rows = len(A)
        col = len(A[0])

        C_Mat = [[0 for i in range(col)] for j in range(rows)]

        for r in range(rows):
            for c in range(col):
                C_Mat[r][c] = A[r][c] + B[r][c]

        return C_Mat


print(solve(A,B))

def subtract_mat(A,B):
    rows = len(A)
    col = len(A[0])

    C_Mat = [[0 for i in range(col)] for j in range(rows)]

    for r in range(rows):
        for c in range(col):
            C_Mat[r][c] = A[r][c] - B[r][c]

    return C_Mat

print(subtract_mat(A,B))
