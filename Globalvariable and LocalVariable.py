x=24#global variable
y=56
def multi():
    z=x*y
    print("multi=",z)
print("x=",x)
print("y=",y)
multi()

def add():#function definition
    a=34#local variable
    b=45
    print("add=",a+b)
add() #function calling