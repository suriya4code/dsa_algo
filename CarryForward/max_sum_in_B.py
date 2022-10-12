# You are given an integer array A of size N.

# You have to pick B elements in total. Some (possibly 0) elements from left end of array A and some (possibly 0) from the right end of array A to get the maximum sum.

# Find and return this maximum possible sum.

# NOTE: Suppose B = 4, and array A contains 10 elements, then

# You can pick the first four elements or can pick the last four elements, or can pick 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can pick.

import math


def Solve(A,B):
    #prefix sum array
    ps = []
    ps.append(A[0])
    for j in range(1,len(A)):
        ps.append(A[j] + ps[j-1])
    suff = [0] * len(A)
    suff[-1] = A[-1]
    for i in range(2, len(A)+1):
        suff[-i] = suff[-i+1]+ A[-i]
    
    max_sum = -math.inf
    for i in range(B+1):
        if i == 0:
            sum_of_L_R = suff[i-B]
        elif i == B:
            sum_of_L_R = ps[i-1]
        else:
            sum_of_L_R = ps[i-1] + suff[i-B]
        if sum_of_L_R > max_sum:
            max_sum = sum_of_L_R
    
    return max_sum

A = [5,-2,3,1,2]
A = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
B = 48

A  = [1,2,3,4,5]
B = 3

# A = [ 1,-2,3,-4]
# B = 2

print("MAx possible sum of sub array => ", Solve(A,B))