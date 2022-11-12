
A = [1, 2, 3, 4, 5]
B = [[0,2], [1,4]]

def solve(A,B):
    N = len(A)
    res = []
    pse = []
    pse.append(0)
    for i in range(1,N):
        if i % 2 == 0:
            pse.append(pse[i-1])
        else:
            pse.append(pse[i-1]+A[i])
    # print(pse)
    for j in B:
        s = j[0]
        e = j[1]
        if s == 0:
            sum_of = pse[e]
        else:
            sum_of = pse[e]-pse[s-1]
        res.append(sum_of)
    return res


print(solve(A,B))