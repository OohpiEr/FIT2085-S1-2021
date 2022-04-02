array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,]
size = 20

first = int(input("Input first index (inclusive): "))
last =  int(input("Input last index (inclusive): "))
#assume last < len(array)
#assume first <= last

subsize =  last-first+1
subarray = [0] * subsize

for i in range (0, subsize):
    temp = array[first+i]
    subarray[i] = temp
    print(subarray[i], end= ' ')

print()
