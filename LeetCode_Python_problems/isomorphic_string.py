# Input: s = "egg", t = "add"
# Output: true

def solve(s , t):
    l = len(s)
    for i in range(1,l):
        if s[i] == s[i-1]:
            if t[i] != t[i-1]:
                return False
        else:
            if t[i] == t[i-1]:
                return False
    return True
            

s = "badc"
t = "baba"
print(solve(s, t))