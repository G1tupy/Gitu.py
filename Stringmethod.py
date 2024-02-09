# # Using single quotes
# my_string_single = 'This is a string using single quotes.'
# # Using double quotes
# my_string_double = "This is a string using double quotes."
# # You can also use triple quotes for multi-line strings
# multi_line_string = '''This is a multi-line string.
# It spans multiple lines and uses triple quotes.'''

# print("my_string_single: ",my_string_single)
# print("my_string_double: ",my_string_double)
# print("multi_line_string: ",multi_line_string)



#access the string
# my_String="Hello World!"
#  #         0123456789101112
# print("my_String[0]=",my_String[0])
# print("len(my_String)=",len(my_String))
# print("my_String[7]=",my_String[7])

# #Negative index
# str="Hello World!"
# print("str[-1]=",str[-1])
# print("str[-12]=",str[-12])


# #Slicing index
# str="Hello World!"
# print("str[:]=",str[:])#entire string it will print
# print("str[:5]=",str[:5])# start to end-1 will print
# print("str[6:]=",str[6:])#start to entire string print
# print("str[:8:2]=",str[:11:2])#string with step size

#String Length
# my_string = "Hello, World!"
# length = len(my_string) # 13
# print("length of string: ",length)

#Iterating Over Characters
# my_string = "Hello, World!"
# for char in my_string:
#     print(char,end="")


# str1 = "Hello, "
# str2 = "World!"
# result = str1 + str2
# # the result will be "Hello, World!"
# print(result)

#repetition (*)
# word="python "
# repeted_word_count=word*4
# print("repeted word count: ",repeted_word_count)

#Membership (in and not in):
# sentence = "This is a sample sentence."
# check1="sample"
# check2="example"
# print(check1 in sentence)#true
# print(check2 in sentence)#false
# print(check1 not in sentence)#false
# print(check2 not  in sentence)#true


#String Formatting (% or .format())
# name = "Alice"
# age = 30
# formatted_str = "My name is %s, and I am %d years old." % (name, age)
# print("formated string: ",formatted_str)
# # formatted_str will be "My name is Alice, and I am 30 years old."
# formatted_str = "My name is {}, and I am {} years old.".format(name, age)
# # formatted_str will be "My name is Alice, and I am 30 years old."
# print("formated string: ",formatted_str)

# rollno=2
# marks=9
# name="kunal"
# formatted_str="my name is %s , i  obtained marks %f and my rollno is %d" %(name,marks,rollno)
# print(formatted_str)
# formatted_str="my name is {} , i  obtained marks {} and my rollno is {}" .format(name,marks,rollno)
# print(formatted_str)
# formatted_str="my name is {0} , i  obtained marks {1} and my rollno is {2}" .format(name,marks,rollno)
# print(formatted_str)
# formatted_str="my name is {1} , i  obtained marks {0} and my rollno is {2}" .format(name,marks,rollno)
# print(formatted_str)


# str1 = "apple"
# str2 = "banana"
# result1 = str1 == str2 # False
# print("str1 == str2: ",result1)
# result2 = str1 != str2 # true
# print("str1 != str2: ",result2)
# result3 = str1 < str2#true
# print("str1 < str2: ",result3)
# result4 = str1 > str2#false
# print("str1 > str2: ",result4)


#Using a for Loop
# text = "Hello, World!"
# for char in text:
#     print(char,end=" ")

# Using a while Loop       012
# text=input("enter text")#abc
# index=0#initialization
# while index<len(text):
#     print(text[index],end=" ")
#     index+=1#0+1=1

# string=input("enter string")#kunal
# reverse_str=""
# for i in string:
#     reverse_str=i+reverse_str#k
# print("reverse string :",reverse_str)   

#kunal 
#k+""=k
#u+k=uk
#n+uk=nuk
#a+nuk=anuk
#l+anuk=lanuk



# original_string = "welcome\nto\nthis world"
# modified_string = original_string.replace("\n", " ")

# print(modified_string)


# string = input("Enter string with newline characters:\n")

# new_str = string.replace("\n", " ")
# print(new_str)

# Example using f-strings (Python 3.6+)
# name="mohit"
# rollno=4
# marks=78.8
# string=f"name is {name},rollno is {rollno} and marks is {marks}"
# print("steing :",string)

# #Example using format.method

# name = "Alice"
# age = 30
# score = 95.5
# formatted_str = "Name: {}, Age: {}, Score: {:.2f}".format(name, age, score)
# print(formatted_str)

# str1="Emma-is-a-data-scientist"
# print("original string: ",str1)
# str2=str1.split("-")#modified string it will return list
# print("after split string: ",str2)
# for sub in str2:
#     print(sub,end=" ")

# nput_string = "Hello12345World"
# result_string = ''
# for char in input_string:
#  if not char.isdigit():
#    result_string += char
# print(result_string) # Output: "HelloWorld"   