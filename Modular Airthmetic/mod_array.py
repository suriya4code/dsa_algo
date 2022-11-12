# You are given a large number in the form of a array A of size N where each element denotes a digit of the number.
# You are also given a number B. You have to find out the value of A % B and return it.

# Problem Constraints
# 1 <= N <= 10^5
# 0 <= Ai <= 9
# 1 <= B <= 10^9

A = [1, 4, 3]
B = 2
A = [ 1, 8, 4, 5, 0, 8, 0 ]
B = 9

def mod_array(A,B):
    N = len(A)
    ans = 0
    r = 1
    for i in range(N-1,-1,-1):
        ans += ((A[i]%B) * r)%B
        r = (10*r)%B
    return ans

print(mod_array(A,B))