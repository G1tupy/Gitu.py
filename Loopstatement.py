#0->start point
#n->end point
#2 -> step size
# #even number series using for loop
# n=int(input("enter number"))
# for i in range(0,n,2):
#     print(i)


# #reverse number series using for loop
# n=int(input("enter number"))
# for i in range(n,0,-2):
#     print(i)


# str="Kiran"
# for i in str:
#     print(i)

#for loop with list
# fruit_li=["Apple","Mango","Banana"]
# for i in fruit_li:
#     print(i)

#table using for loop
# num=int(input("enter number"))
# for i in range(1,11):
#     print(num*i)

#for loop with else part
# fruit_li=["Apple","Mango","Banana"]
# for i in fruit_li:
#     print(i)
# else:
#     print("this is else block")


#for loop with break and else
# Student=["Mahi","Sneha","Tarishi"]
# for i in Student:
#     if i=="Sneha":#sneha
#         break#stop
#     else:
#         print(i)#Mahi
# else:
#     print("this is else part")


#1-n
# num=int(input("enter number"))
# i=1#initialize the value
# while(i<=num):#cond
#     print(i)#stat
#     i+=1 #i=i+1 #incr/decre

#n-1
# num=int(input("enter number"))#5
# i=num#5
# while(i>=1):#5>=1,4>=1,3>=1,2>=1,1>=1,0>=1
#     print(i)#5,4,3,2,1
#     i-=1#i=i-1->5-1=4-1=3-1=2-1=1-1=0

#factorial
# num=int(input("enter number"))
# fact=1
# i=1
# while(i<=num):
#     fact=fact*i
#     i+=1
# print("factorial of digit ",num,"is",fact)


#while with else
# num=int(input("enter number"))
# i=2
# while(i<=num):
#     print(i)
#     i+=2
# else:
#     print("this is else part")


#while loop with break
# num=int(input("enter number"))#5
# i=1
# while(i<=num):#5
#     if i==3:#3==3
#         break
#     else:
#         print(i)#1,2
#         i+=1#2,3
# else:
#     print("this is else part")

#while loop with string
# str="Python"
# print("length=",len(str))
# i=0
# while i<len(str):
#     print(str[i])#p,y,t,h,o,n
#     i+=1

#while loop 
li=["apple","mango","banana"]
#      0       1      2
i=0
while(i<len(li)):
    print(li[i])
    i+=1