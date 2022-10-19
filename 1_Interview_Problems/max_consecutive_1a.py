import math


A = [1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1]
# A = [0, 0 ,0]

def maxConsecutive_1(A):
    count = A.count(1)
    N = len(A)
    if count == N: return N
    if count == 0: return 1

    ans = -math.inf

    for i in range(N):
        l = 0
        r = 0
        if A[i] == 0:
            k = i-1
            while k>=0:
                if A[k] == 1:
                    l+=1
                    k -= 1
                else: break

            for j in range(i+1, N):
                if A[j] == 1:
                    r+=1
                else: break
            ans = max(ans, l+r+1)
            print(ans)
    return ans

print(maxConsecutive_1(A))