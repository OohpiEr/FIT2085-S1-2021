secret = 42
guess = int(input("Enter guess: "))
diff = secret - guess

if diff < 0:
    print("Too high")
elif diff == 0:
    print("Good guess!")
else:
    print("Too low")

