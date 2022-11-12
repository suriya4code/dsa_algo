A = 10
B = 2


def DecimalToAnyBase(A,B):
    i = 0
    ans = 0
    while A>0:
        rem = A%B
        ans += (rem * (10**i))
        A = A//B
        i += 1
    return ans



print(DecimalToAnyBase(A,B))