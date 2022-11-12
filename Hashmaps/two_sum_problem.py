A = [2,4,6,6,8]
B = 10

def solve(A, B):
    d = {}
    for i in A:
        if d.get(B-i) != None:
            return True
        else:
            d[i]=i
    return False

def solve2(A, B):
    d = set()
    for i in A:
        if B-i in d:
            return True
        else:
            d.add(i)
    return False

print(solve2(A,B))
