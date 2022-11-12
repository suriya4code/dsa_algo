A = [1, -2, 1, 2]


def solve2(A):
    n = len(A)
    l = 0
    if A[0]==0:
        l=1
    ps = []
    ps.append(A[0])
    for i in range(1,n):
        if A[i] == 0:
            l = max(l, 1)

        pse = ps[i-1]+A[i]
        
        if pse == 0:
            l = max(l,i+1)

        ps.append(pse)

    k = {}
    for i in range(n):
        if k.get(ps[i]) != None:
            t_l = i - k[ps[i]]
            l = max(l, t_l)
        else:
            k[ps[i]]=i

    return l

print(solve2(A))