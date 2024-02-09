#IF IS ELSE LADDER
marks=int(input("Enter marks"))
if(marks<=100 and marks>=80):
    print("A grade")
elif(marks<80 and marks>=60):
     print("B grade")
elif(marks<60 and marks>=40):
      print("C grade")
else:
     print("Fail")           