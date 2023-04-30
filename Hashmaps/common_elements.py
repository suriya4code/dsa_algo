A = [1, 2, 2, 1]
B = [2, 3, 1, 2]


def solve(A, B):
    res = []
    for i in A:
        if i in B:
            res.append(i)
            B.remove(i)
    return res


def solve2(A, B):
    d = {}
    for i in A:
        if d.get(i) == None:
            d[i]=1
        else:
            d[i] = d[i]+1
    res = []
    for j in B:
        if d.get(j)!= None and d[j] !=0:
            res.append(j)
            d[j] -= 1
    
   
    return res
                
            



print(solve2(A, B))