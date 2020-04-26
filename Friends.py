C=int(input("Enter the amount of your CIB amount: "))
Ci=int(input("Enter the amount of your Citibank amount: "))
A=int(input("Enter the amount of your AAIB amount: "))

def f(C,Ci,A):
    CiE=Ci*16
    x=C+CiE+A
    y=x/16
    z=x/11
    youssef=x/6000
    safi=x/20000
    yy=x/(6000*12)
    sy=x/((20000*12)+200000)
    wahba=(120000*0.7)*16
    t=wahba/x
    print ("Your money in EGP: ", x)
    print ("Your money in USD: ", y)
    print ("Your money in CAD: ", z)
    print ("You have ", youssef, "Youssef")
    print ("You have ", safi, "Safi")
    print ("Youssef needs to work", yy, "years to be equal Fady")
    print ("Safi needs to work", sy, "years to be equal Fady")
    print ("Wahba per year= ", t, "Fady")
    print ("Safi needs to work", wahba/440000, "years to make one Wahba per year")
    print ("Youssef needs to work", wahba/72000, "years to make one Wahba per year")
    
    
f(C,Ci,A)
