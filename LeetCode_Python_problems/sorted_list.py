

def solve(list1, list2):
    list1 = list(list1)
    l = list1.extend(list2)
    return sorted(list1)

list1 = [1,4, 5]
list2 = [1,2,3]
print(solve(list1, list2))