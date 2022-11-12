# Problem Description
# Given three 2-digit integers, A, B, and C, find out the minimum number obtained by concatenating them in any order.

# Return the minimum result obtained.



# Problem Constraints
# 10 <= A, B, C <= 99

A = 10
B = 20
C = 30

def solve(A, B, C):
    max_no = max(A, B, C)
    min_no = min(A, B, C)
    rem = (A+B+C)-max_no-min_no
    return (min_no* 10**4) + (rem * 10**2)+max_no

print(solve(A, B,C))
