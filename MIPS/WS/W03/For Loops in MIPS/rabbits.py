previous = -1
current = 1

size = int(input("Input size: "))

for i in range(0, size, 1):
    current = current + previous
    previous = current - previous
    print(current, end=' ')
print()


previous = -1
current = 1

size = int(input("Input size: "))

i = 0
while i < size:
    current = current + previous
    previous = current - previous
    print(current, end=' ')
    i += 1
print()
