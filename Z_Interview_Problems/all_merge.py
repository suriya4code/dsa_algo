class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self) -> str:
        return f"[{self.start}, {self.end}]"

lst = [ (54, 75), (56, 60), (61, 86), (22, 43), (56, 87), (32, 53), (14, 81), (64, 65), (9, 42), (12, 33), (22, 58), (84, 90), (27, 59), (41, 48), (43, 47), (22, 29), (16, 23), (41, 72), (15, 87), (20, 59), (45, 84), (14, 77), (72, 93), (20, 58), (47, 53), (25, 88), (5, 89), (34, 97), (14, 47) ]
int_list = [Interval(i[0],i[1]) for i in lst]

def solve(A):
    n = len(A)
    cur = A[0]
    s,e,i = 0,1,1
    res = []
    new_cur = False
    import operator
    sorted(A,key=operator.attrgetter('start'))

    while i<n:
        if cur.start>A[i].end:
            res.append(A[i])
            cur = A[i]
        elif cur.end<A[i].start:
            if new_cur:
                res.append(cur)
                new_cur = False
            res.append(A[i])
            cur = A[i]
        elif cur.end<A[i].start:
            res.append(cur)
        else:
            #overlap
            cur.start= min(A[i].start,cur.start)
            cur.end= max(A[i].end,cur.end)
            new_cur = True
            
        i+=1
    if new_cur: res.append(cur)
    return res

print(solve(int_list))

