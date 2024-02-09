for i in range(1,6):
    for j in range(1,6):
        #j=1 for  vertical line
        #i=1 for top horizontal line
        #i=5 for bottom horizontal line
        if j==1 or i==1 or i==5:
         print("* ",end="")
        else:
         print("  ",end="")
    print("")

