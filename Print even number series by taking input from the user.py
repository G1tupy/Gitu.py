# Take input from the user
limit = int(input("Enter the limit for the even number series: "))

# Print even numbers up to the given limit
print("Even numbers up to", limit, "are:")
for i in range(2, limit + 1, 2):
    print(i)
