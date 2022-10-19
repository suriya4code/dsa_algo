
A = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]

def solve(A):
    rows = len(A)
    col = len(A[0])
    result = []
    for c in range(col):
        sum_of_col = 0
        for r in range(rows):
            sum_of_col += A[r][c]
        result.append(sum_of_col)
    return result

def row_sum(A):
    rows = len(A)
    col = len(A[0])
    result = []
    for r in range(rows):
        sum_of_col = 0
        for c in range(col):
            sum_of_col += A[r][c]
        result.append(sum_of_col)
    return result


print(solve(A))
print(row_sum(A))