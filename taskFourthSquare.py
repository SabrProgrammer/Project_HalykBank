# Task fourth square
# Given an integer x, determine whether it is the square of any integer

# Enter number x
x = int(input("Enter integer number:"))

# Check number x to square of any number
check = False

for i in range(x):
    if i * i == x:
        check = True
        print("This number (x) is the square of " + str(i))
        print(str(i) + " * " + str(i) + " = " + str(x))
        break

if not check:
    print("This number is not a square of any number")
