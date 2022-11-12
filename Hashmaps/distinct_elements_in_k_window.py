A = [1,2,3,4,3,5,6,3,4,5,6,7]
B = 4



def solve(A,B):
    n = len(A)
    sum_of = 0
    for i in range(n-B+1):
        s= i
        e = i+B
        ds = set(A[s:e])
        sum_of += len(ds)
    return sum_of

A = [1, 2, 1, 3, 4, 3]
B = 3

def solve2(A, B):
    n = len(A)
    res = []
    d = {}
    for i in range(B):
        if d.get(A[i]) == None:
            d[A[i]]=1
        else:
            d[A[i]] = d[A[i]]+1
    res.append(len(d))

    for j in range(B,n):
        s = j-B
        e = j

        #remove start index
        s_fq = d.get(A[s])
        if s_fq == 1:
            del d[A[s]]
        else:
            d[A[s]] = s_fq-1
        
        #add end index
        e_fq = d.get(A[e])
        if e_fq == None:
            d[A[e]] = 1
        else:
            d[A[e]] = e_fq+1
        
        res.append(len(d))
    return res
        


        
    


   
    

print(solve2(A,B))