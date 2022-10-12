

A = [2,3,4,5,6,7]
s = 3
e = 5
def printSubArray(A, s, e):
    for i in range(s,e+1):
        print(A[i])

printSubArray(A, s,e)


def sum_of_Subarray(A, s, e):
    sum_of = 0
    for i in range(s,e+1):
        sum_of += A[i]
    return sum_of

print(sum_of_Subarray(A, s, e))