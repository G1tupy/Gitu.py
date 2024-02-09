# def addition():
#     a=34
#     b=45
#     add=a+b
#     print("add=",add)

# addition()

#function with parameter

# def fruits(name):
#     print("i like",name)#apple#kiwi
# fruits("Apple")
# fruits("kiwi")

#function with default parameter
# def fruits(name="Mit",fruit="mango"):
#     print(name,"likes",fruit)
# fruits()
# fruits("sneha","Kiwi")

#function with return keyword
# def square(n):
#     return n**2

# num=int(input("enter number"))
# print("square=",square(num))
# result=square(3)
# print("result=",result)

#passing list as a argument
# def fruit(fruitlist):
#     for i in fruitlist:
#         print("i like",i)

# mylist=["apple","mango","banana"]
# fruit(mylist)

#arbitory argument
# def fruits(*fruitlist):
#     print("i like",fruitlist[0])
#     print("i like",fruitlist[1])
#     print("i like",fruitlist[2])
# fruits("apple","mango","kiwi")

#def fruits(*fruitlist):
    #print("i like",fruitlist[0])
    #print("i like",fruitlist[1])
    #print("i like",fruitlist[2])
#fruits("apple","mango","kiwi")


#    if(num>1):#5>1,4>1,3>1,2>1
#        return num*factorial(num-1)#5*4=20*3=60*2=120*1=120
#    else:
#        return 1




#no=int(input("enter number"))#5
#factorial(no)
#print("factorial of",no,"is",factorial(no))
#def factorial(num):
#    if(num>1):#5>1,4>1,3>1,2>1
#        return num*factorial(num-1)#5*4=20*3=60*2=120*1=120
#    else:
#        return 1

# no=int(input("enter number"))#5
# factorial(no)
# print("factorial of",no,"is",factorial(no))

# def fruit(fruitlist):
#     pass
# def fruit(name):
#     print("i like" , name)
# fruit("Grapes")    


#Recursion
# def myFunction(): #defination
#     print("Heyyyy")
#     myFunction() #inside calling himself
# myFunction()

# def table(num):
#     if num<=50:
#         print(num,end=" ")
#         num+=5
#         table