A = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]


def diagnol_sum(A):
    rows = col= len(A)
    sum_of_dia = 0
    for r in range(rows):
            sum_of_dia += A[r][r]
    return sum_of_dia


print(diagnol_sum(A))