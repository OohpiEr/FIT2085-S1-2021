size = int(input("Array length: "))
the_list = [None] * size

for i in range(len(the_list)): 
    the_list[i] = int(input("Enter num: "))
    if i == 0 or min_item > the_list[i]:
        min_item = the_list[i]

print("The minimum element in this list is " + str(min_item))