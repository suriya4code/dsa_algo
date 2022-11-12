# Given an integer A representing a year, Return 1 if it is a leap year else, return 0.

# A year is a leap year if the following conditions are satisfied:

# The year is multiple of 400.
# or the year is multiple of 4 and not multiple of 100.

A = 2020
A = 1999
A = 1300
A = 1200

def solve(A):
    if A%4==0 and A%400==0:
        return 1
    elif A%4==0 and A%100!=0:
        return 1
    return 0
print(solve(A))