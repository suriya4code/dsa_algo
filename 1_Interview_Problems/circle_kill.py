A = 11


def last_man_standing(A):
    pc = 0
    for i in range(A):
        if 2**i > A:
            pc = 2**(i-1)
            break
    
    #find the person holding knives after pc kill
    return (2*(A-pc) + 1)


print(last_man_standing(A))