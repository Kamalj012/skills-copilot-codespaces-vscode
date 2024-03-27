# Initialize the first two numbers in the sequence
num1 = 0
num2 = 1

# Print the first two numbers
print(num1)
print(num2)

# Generate the Fibonacci series
while num1 + num2 <= 100:
    # Calculate the next number in the sequence
    next_num = num1 + num2
    
    # Print the next number
    print(next_num)
    
    # Update the values of num1 and num2
    num1 = num2
    num2 = next_num