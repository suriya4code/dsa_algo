A = 5
B = 4

#11000



def solve(A,B):
        l = A+B
        fst = 10**(l-1)
        sec = 10**B
        N = fst+sec
        i = 0
        ans = 0
        while N>0:
            rem = N%10
            N = N//10
            ans += rem* (B**i)
            i+=1
        return ans

print(solve(A,B))