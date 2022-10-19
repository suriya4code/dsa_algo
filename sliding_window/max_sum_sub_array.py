import math


A = [11,2,3,4,5,6,7,8,9,10,11]

def max_subArray(A,N,k):
    ans = -math.inf
    for i in range(N-k+1):
        s = i
        e = k+i-1
        sum_of = 0
        for j in range(s,e+1):
            sum_of += A[j]
        ans = max(ans,sum_of)
    return ans

def max_subArray_prefix(A,N,k):
    ps = []
    ps.append(A[0])
    for j in range(1,len(A)):
        ps.append(A[j] + ps[j-1])
    ans = -math.inf
    for i in range(N-k+1):
        s = i
        e = k+i-1
        if s == 0:
            sum_of = ps[e]
        else:
            sum_of = ps[e] - ps[s-1]
        ans = max(ans,sum_of)
    return ans


#Sliding technique trail in python

def max_subarray_sliding(A, N, k):
    sum_of = 0
    ans = -math.inf
    for i in range(k):
        sum_of = sum_of + A[i]
    for s in range(1, N-k+1):
        e = k+s-1
        sum_of = sum_of - A[s-1] + A[e]
        ans = max(ans, sum_of)
    return ans

print(max_subArray_prefix(A,11,4))
print(max_subarray_sliding(A,11,4))