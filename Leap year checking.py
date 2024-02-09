def is_leap_year(year):
    if (year % 4 == 0): #year is divided by 4
        return True
    else:
        return False
year_to_check = int(input("enter the year"))  
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
    