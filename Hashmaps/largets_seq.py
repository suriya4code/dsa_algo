A = [-1, 8, 5, 2, 3,7,1,4,9]
B = 1



def solve(A,B):
    s = set(A)
    l = 0
    for i in A:
        count = 1
        j = i
        flag = True
        while flag:
            if i-1 in s:
                flag = False
                continue
            if j+1 in s:
                count +=1
                j+=1
            else:
                flag = False
        l = max(l, count)
    return l
        

print(solve(A,B))