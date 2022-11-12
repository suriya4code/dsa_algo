from time import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        print("Starting time calculation")
        result = func(*args, **kwargs)
        print("Finished time calculation")
        end = time()
        print((end-start)*1000)
        return result
    return wrapper


A = [2,3,4,5,6,5,4,3,2]
A = [1, 2, 1, 1]
B = [1, 2]

@calculate_time
def solve(A, B):
    d = {}
    k = []
    for i in A:
        if i not in k:
            d[i]=A.count(i)
            k.append(i)
    res = []
    for i in B:
        res.append(d[i] if i in k else 0)
    return res

print(solve(A,B))

@calculate_time
def solve2(A, B):
    d = {}
    for i in A:
        if d.get(i) == None:
            d[i]=1
        else:
            d[i] = d[i]+1
    res = []
    for i in B:
        if d.get(i) != None:
            res.append(d[i])
        else:
            res.append(0)
    return res    

print(solve2(A,B))
