

A = [[1,2,3],[4,5,6],[7,8,9]]
# A = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]


def rotate_90_square_matrix(A):
    rows = len(A)
    col = len(A[0])
    # res = [[0 for i in range(rows)] for j in range(col)]
    for r in range(rows):
        for c in range( r+1, col):
            A[c][r],A[r][c] = A[r][c], A[c][r]
    for r in range(rows):
        start = 0
        end = rows-1

        while start < end:
            A[r][start],A[r][end] = A[r][end],A[r][start]
            start += 1
            end -= 1
    return A

print(rotate_90_square_matrix(A))
