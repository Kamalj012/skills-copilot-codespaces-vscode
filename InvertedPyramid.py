def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

# Prompt the user to enter the number of rows
num_rows = int(input("Enter the number of rows: "))

# Generate the inverted pyramid
inverted_pyramid(num_rows)