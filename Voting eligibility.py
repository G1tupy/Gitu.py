def check_eligibility(age):
    if age >= 18:#if the condition is true
        print("You are eligible to vote")#then print the person is eligible to vote 
    else: 
        print("you are not eligible to vote")# then it will print the person is not eligible to vote 
user_age = int(input("Enter your age: ")) # user input for age
check_eligibility(user_age) # Check the eligibility   