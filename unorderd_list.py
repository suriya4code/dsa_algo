K = 5
A = "1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2"

# K = int(input())
# A = input().split(" ")

A = A.split(" ")
B = set(A)
N = (len(A)-1)//K

for i in B:
    if A.count(i) != K:
        print(i)
        break


def solve(ROOM_LIST):
    # ROOM_LIST = input().split() #31 
    # "1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2"
    ROOM_SET = set(ROOM_LIST) #7 
    #1,2,3,4,5,6,8

    for ele in list(ROOM_SET):
        ROOM_LIST.remove(ele) #25
    CAPTAIN_ROOM_NUM = ROOM_SET.difference(set(ROOM_LIST)).pop()
    print(CAPTAIN_ROOM_NUM)

solve(A)

print({1,2,3,4}.pop())