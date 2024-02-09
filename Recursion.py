def factorial(n):
    if n == 0 or n == 1:  # Base case: if n is 0 or 1, return 1
        return 1
    else: #recursive case : multiply n with the factorial of (n-1)
        return n * factorial(n - 1)

# Calculate the factorial of 5
result = factorial(5)
print("Factorial of 5 is:", result)