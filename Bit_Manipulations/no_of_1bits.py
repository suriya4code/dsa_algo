A = 10
def numSetBits(A):
    count = 0
    while A>0:
        if A & 1 == 1:
            count += 1
        A = A>>1
    return count

def numSetBits2( A):
    ret = 0
    while A != 0:
        # rightmost set bit becomes unset
        A = A & (A - 1)
        ret += 1
    return ret

print(numSetBits(A))
print(numSetBits2(A))
