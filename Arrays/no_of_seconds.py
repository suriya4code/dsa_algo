# Given an integer array A of size N. In one second, you can increase the value of one element by 1.

# Find the minimum time in seconds to make all elements of the array equal.

def solve(A):

    import math
    max_no = -math.inf
    for i in range(len(A)):
        if (A[i] > max_no):
            max_no = A[i]
    sum_of = 0
    for i in A:
        sum_of = sum_of + (max_no-i)

    return sum_of


 

print(solve([1,2,3,4]))