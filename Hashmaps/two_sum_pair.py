A = [3, 5, 1, 2]
B = 8
A = [1, 2, 1, 2]
B = 3

# A = [ 9, 18, 17, 17, 6, 16, 13, 11, 15, 7 ]
# B = 15

def solve(A,B):
    d = {}
    for i in A:
        if d.get(i) == None:
            d[i]=1
        else:
            d[i] = d[i]+1
    count = 0
    for j in A:
        if d.get(B-j)!=None:
            count += d.get(B-j)
    return count//2

print(solve(A, B))