



def bulbs(A):
    opr = 0
    for i in A:
        if opr %2 == 1:
            i = 1-i
        if i == 0:
            opr += 1
    return opr