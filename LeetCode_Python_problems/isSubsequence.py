# Input: s = "abc", t = "ahbgdc"
# Output: true

def solve(s, t):
        l = len(s)
        if l == 0:
            return True
        i = 0
        for j in t:
            if j == s[i]:
                if i< l-1:
                    i+=1
                else:
                    return True
        if i == l:
            return True
        return False


    

s = "abc"
t = "ahbgdc"

# s= "axc"
# t = "ahbgdc"

print(solve(s, t))
