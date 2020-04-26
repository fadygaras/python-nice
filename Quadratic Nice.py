print("This is a quadratic formula calculator to get the values of x")
print("Please enter the values of a, b and c")

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

def Quadratic(a,b,c):
    temp = (b**2-(4*a*c))
    sqrt = temp**(.5)
    h=-b+sqrt
    h2=-b-sqrt
    w=2*a
    x=(h/w)
    x2=(h2/w)
    if temp>=0:
        print("   x1= ",x)
        print("or")
        print("   x2= ",x2)
    else:
        print("Kosom Safi")
def MinMax(a,b):
    x=(-b)/(2*a)
    y=((a*(x**2))+(b*x)+c)
    if ((2*a)<0):
        print("The maximum value occurs at x= ", x, "and y= ", y)
    else:
        print("The minimum value occurs at x= ", x, "and y= ", y)
        
Quadratic(a,b,c)
MinMax(a,b)

