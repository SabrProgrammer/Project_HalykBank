# Task third snake
# There is a two-dimensional array, output the values in one sheet in the snake order

# A basic code for matrix input from user
row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
print("Like this:")
print("1")
print("2")
print("3")
print("...")
print()

# For user input
for i in range(row):  # A for loop for row entries
    a = []
    for j in range(column):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

print()

# For printing the matrix
print("Array:")
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()

# Snake list
snakeList = []

# For list in snake order
for i in range(row):
    if i % 2 == 0:
        for j in range(column):
            snakeList.append(matrix[i][j])
    else:
        j = column - 1
        while j >= 0:
            snakeList.append(matrix[i][j])
            j = j - 1

# For printing the list
print()
print("List in snake order:")
print(snakeList)
