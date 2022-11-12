A = 4
B = 1

def DecimalToAnyBase(A,B):
    i = 0
    while True:
        if B**i>A:
            break
        i+=1
        
    hp = i-1
    ans = 0

    while A>1:
        ans += 10**hp
        A = A-(B**hp)
        hp -= 1
    return ans

def solve(A,B):
    # N = DecimalToAnyBase(A,2)
    if (A >> B) & 1 == 0:
        return 0
    else: return 1

print(solve(49,0))

