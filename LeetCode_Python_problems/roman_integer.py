#https://leetcode.com/problems/roman-to-integer/
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


def solve(s):
    hm = {"I":1, "V":5,"X":10, "L":50, "C":100,"D":500,"M":1000}
    n = len(s)
    # s = s[::-1]
    sum_of = 0
    prev_val = 0
    for i in range(n-1,-1,-1):
        val = hm[s[i]]
        if val < prev_val:
            sum_of -= val
        else: sum_of += val
        prev_val = val

    return sum_of

s = "IVV"
s = "MCMXCIV"

print(solve(s))

