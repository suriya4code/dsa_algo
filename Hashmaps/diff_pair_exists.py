
A = [5, 10, 3, 2, 50, 80]
B = 78

A = [ -10, 20 ]
B = 30

A = [ 637, -466, 556, 993, -824, 705, -38, -452, 881, -700, -587, -359, 855, -145, 142, 462, 611, -123, -576, -322, 752, -557, -704, -327, -960, 313, -125, -928, -182, -390, 17, -68, -888, -305, 169 ]
A.sort()

B = 570


def solve(A, B):
    d = {}
    for i in A:
        if d.get(B+i) != None or  d.get(i-B) != None:
                return 1
        # else:
        #     if d.get(i-B) != None:
        #         return 1
        d[i]=i
    return 0

print(solve(A,B))