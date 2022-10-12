# You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
# But the sum must not exceed B.

# Example Input
# Input 1:
A = 5
B = 12
C = [2, 1, 3, 4, 5]
# Input 2:
# A = 3
# B = 1
# C = [2, 2, 2]

# Example Output
# Output 1:
# 12
# Output 2:

# 0
def maxSubarray(A, B, C):
    if A==1:
        return C[0]
    max_sum = 0
    for s in range(A):
        for e in range(s,A):
            sum_of = 0
            for i in range(s,e+1):
                sum_of += C[i]
            # print("*******", s)        
            # print(sum_of)
            if sum_of > max_sum and sum_of <= B :
                max_sum = sum_of
    return max_sum

def maxSubarray2(A, B, C):
    if A==1:
        return C[0]
    max_sum = 0
    ps = []
    ps.append(C[0])
    for i in range(1, A):
        ps.append(ps[i-1] + C[i])
    for s in range(A):
        sum_of = 0
        for e in range(s,A):
            if s==0:
                sum_of = ps[e]
            else:
                sum_of = ps[e]-ps[s-1]
        # print("*******", s)        
        # print(sum_of)
            if sum_of > max_sum and sum_of <= B :
                    max_sum = sum_of
    return max_sum

def maxSubarray_Sln(A, B, C):
    ans = 0
    for i in range(A):
        sum = 0
        for j in range(i, A):
            sum += C[j]
            if (sum <= B):
                ans = max(ans, sum)
            else:
                break
    return ans
A = 9
B = 78
C = [ 7, 1, 8, 5, 8, 5, 3, 3, 5 ]


A = 9
B = 14
C = [ 1, 2, 4, 4, 5, 5, 5, 7, 5 ]

# A = 10
# B = 120
# C = [1,2,3,4,2,3,4,3,7,5]
print(maxSubarray(A,B,C))
print(maxSubarray2(A,B,C))
print(maxSubarray_sln(A,B,C))