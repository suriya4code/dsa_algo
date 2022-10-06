# Given an array A of size N.
# You need to find the sum of Maximum and Minimum element in the given array.

def Solve(A):
    import math
    max_no = -math.inf
    min_no = math.inf

    for i in range(0,len(A)):
        if A[i] < min_no:
            min_no = A[i]
        if A[i] > max_no:
            max_no = A[i]
    return max_no+min_no


print("Solve = > ", Solve([1,2,3,-4]))