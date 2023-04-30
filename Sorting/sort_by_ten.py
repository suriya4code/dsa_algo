import functools
def compare(val1, val2):
    tens_digit1 = (val1 // 10 ) % 10
    tens_digit2 = (val2 // 10 ) % 10
    if (tens_digit1 == tens_digit2):
        return val2 - val1
    return tens_digit1 - tens_digit2

A = [15, 11, 7, 19]

def solve(A):
    A = sorted(A, key = functools.cmp_to_key(compare))
    return A

print(solve(A))