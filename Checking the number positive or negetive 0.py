def check_number(num):
    if num > 0: #10
        print("The number is positive.") #It will print positive if the number starts with +
    elif num < 0: #-4
        print("The number is negative.") #It will print negative if the number starts with -
    else: 
        print("The number is zero.") # it will print the number is zero
user_num = float(input("Enter a number: ")) # Get user input for the number
check_number(user_num)# Check the number