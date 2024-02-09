# Get user input
num = int(input("Enter a number: "))
factorial = 1 # This is the initialize variables
current_num = 1
while current_num <= num:  # Calculate factorial using while loop
    factorial *= current_num
    current_num += 1

print(f"The factorial of {num} is: {factorial}")
