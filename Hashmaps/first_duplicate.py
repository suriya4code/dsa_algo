A = [10, 5, 3, 4, 3, 5, 6]


def solve(A):
    k = {}
    for i in A:
        if A.count(i)>1:
            return i
    return -1