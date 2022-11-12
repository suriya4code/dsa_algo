# Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

# Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.


A = [1,2,3,4,5]
A = [ 5, 1, 10, 1 ]

def Solve(A):
    res = []
    for i in range(len(A)):
        prd = 1
        for s in range(i,0,-1):
            prd *= A[s-1]
        for j in range(i+1,len(A)):
            prd *= A[j]
        
        res.append(prd)
    return res

print(Solve(A))

def solve_sltn(self, A):
    n = len(A)
    pref = [0] * n
    suff = [0] * n
    pref[0] = A[0]
    for i in range(1,n):
        pref[i] = pref[i - 1] * A[i]
    suff[n - 1] = A[n - 1]
    for i in range(n-2 , -1, -1):
        suff[i] = suff[i + 1] * A[i]
    ans = [0] * n
    for i in range(n):
        if(i == 0):
            ans[i] = suff[i + 1]
        elif i == n - 1:
            ans[i] = pref[i - 1]
        else:
            ans[i] = pref[i - 1] * suff[i + 1]
    return ans