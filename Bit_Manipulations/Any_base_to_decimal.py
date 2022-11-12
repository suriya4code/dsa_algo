A = 22 
B = 3


def solve(A,B):
        i = 0
        ans = 0
        while A>0:
            rem = A%10
            A = A//10
            ans += rem* (B**i)
            i+=1
        return ans

print(solve(A,B))