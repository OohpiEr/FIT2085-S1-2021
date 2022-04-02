def print_intersection(list1: list, list2: list) -> list:
    result = []
    for i in list1:
        for j in list2:
            if i == j:
                result.append(i)
    for i in result:
        print(i)

l1 = [2, 4, 8]
l2 = [9, 3, 2]
print_intersection(l1,l2)