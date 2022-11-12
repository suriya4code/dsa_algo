# You are given A, B and C .
# Calculate the value of (A ^ B) % C


# Problem Constraints
# 1 <= A <= 109
# 0 <= B <= 105
# 1 <= C <= 109

A = 2**10
B = 3
C = 3

def pow_of(A,B,C):
    return (A**B)%C

def solve(self, A, B, C):
    res = 1
    for i in range(B):
        res = (res * A) % C
    return res

print(pow_of(A,B,C))