# You are given a matrix A, you have to return another matrix which is the transpose of A.

# NOTE: Transpose of a matrix A is defined as - AT[i][j] = A[j][i] ; Where 1 ≤ i ≤ col and 1 ≤ j ≤ row. The tranpose of a matrix switches the element at (i, j)th index to (j, i)th index, 
# and the element at (j, i)th index to (i, j)th index.


A = [[1,2,3],[4,5,6],[7,8,9]]
A = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]


def transpose_square_matrix(A):
    rows = len(A)
    col = len(A[0])
    # res = [[0 for i in range(rows)] for j in range(col)]
    for r in range(rows):
        for c in range( r+1, col):
            A[c][r],A[r][c] = A[r][c], A[c][r]
            
    return A

def transpose_rect_matrix(A):
    rows = len(A)
    col = len(A[0])
    res = [[0 for i in range(rows)] for j in range(col)]
    for r in range(rows):
        for c in range(col):
            res[c][r] = A[r][c]
            
    return res

print(transpose_rect_matrix(A))