# You are given a N X N integer matrix.
#  You have to find the sum of all the minor diagonal elements of A.

# Minor diagonal of a M X M matrix A is a collection of elements A[i, j]
#  such that i + j = M + 1 (where i, j are 1-based).

A = [[1,2,3,4],[5,6,7,8],[9,2,3,4], [5,6,7,8]]


def diagnol_sum(A):
    rows = len(A)
    col = len(A[0])
    sum_of_col = 0
    r = 0
    c = col-1
    while r < rows and c >= 0:
        sum_of_col += A[r][c]
        r += 1
        c -= 1
    return sum_of_col


print(diagnol_sum(A))