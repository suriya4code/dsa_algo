A = [4,1,2,6,9,7]

def Count_triplet(A):
    ans = 0
    N = len(A)
    for i in range(1,N):
        #count of smaller in left
        l = 0
        k = i-1
        while k>=0:
            if A[k] < A[i]:
                l+=1
            k-=1
        #count of greater right element
        r = 0
        for j in range(i+1, N):
            if A[j] > A[i]:
                r+=1
        ans += (l*r)

    return ans


print(Count_triplet(A))

def solve(A):
    n = len(A)
    ans = 0
    for i in range(n):
        l = 0
        r = 0
        for j in range(i):
            if A[j] < A[i]:
                l += 1
        for j in range(i + 1 , n):
            if(A[i] < A[j]):
                r += 1
        ans += (l * r)
    return ans

print(solve(A))