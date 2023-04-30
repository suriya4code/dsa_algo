# You are given A, B and C .
# Calculate the value of (A ^ B) % C


# Problem Constraints
# 1 <= A <= 109
# 0 <= B <= 105
# 1 <= C <= 109

A = 2**10
B = 3
C = 3

A = 0
B = 0
C = 1

def pow_of(A,B,C):
    return (A**B)%C

def solve(A, B, C):
    res = 1
    for i in range(B):
        res = (res * A) % C
    return res%C

def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

A = 79161127
B = 99046373
C = 57263970
# A = 0
# B = 0
# C = 1
print(pow_mod(A,B,C))
print(pow(A,B,C))