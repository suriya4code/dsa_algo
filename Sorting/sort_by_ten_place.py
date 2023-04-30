# Given an array A of N integers. Sort the array in increasing order of the value at the tens place digit of every number.

# If a number has no tens digit, we can assume value to be 0.
# If 2 numbers have same tens digit, in that case number with max value will come first
# Solution should be based on comparator.

# Problem Constraints
# 1 <= N <= 105

# 1 <= A[i] <= 109

A = [15, 11, 7, 19]

def comparator(i):
    return (i//10)%10


def solve(A):
    sorted(A, key=comparator)
    return A

print(solve(A))