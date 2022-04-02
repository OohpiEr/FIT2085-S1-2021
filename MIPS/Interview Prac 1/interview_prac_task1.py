first = int(input("Enter first: "))
second = int(input("Enter second: "))

if first > 0 and second >= 0:
    result = second // first
elif first == second or first < second: 
    result = first * second
else:
    result = second * 2
    
print("Result: " + str(result))