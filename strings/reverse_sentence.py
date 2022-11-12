A = "the sky is blue"
A = "crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv "

def reverse_str(A):
    return A[::-1]

def solve2(A):
    n = len(A)
    A = A[::-1]
    s = 0
    res = ""
    for i in range(n):
        
        if A[i] == " ":
            if i == 0:
                s =1
                continue
            e = i-1
            if s == 0:
                res += reverse_str(A[:e+1]) + " "
            else:
                res += reverse_str(A[s:e+1]) + " "
            s = i
        if i == n-1:
            res += A[n:s:-1]
    return res

def solve(A):
    n = len(A)
    A = A[::-1]
    s = 0
    res = ""
    for i in range(n):
        
        if A[i] == " ":
            if i == 0:
                s =1
                continue
            e = i-1
            if s == 0:
                res += A[e::-1] + " "
            else:
                res += A[e:s:-1] + " "
            s = i
        if i == n-1:
            res += A[n:s:-1]
    return res

print(solve(A))
print(solve2(A))

