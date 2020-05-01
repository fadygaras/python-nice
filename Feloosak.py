def Feloos(C,Ci,A):
    fm=C+(Ci*16)+A
    fd=fm/16
    return fm,fd
    
def So7abak(fm,ypy,spy):
    fpy=fm/ypy
    fps=fm/spy
    return fpy,fps

def Whatif(Am,Eu,St,fm):
    Wi=(Am+Eu+St)+fm
    return Wi
    
def main():
    C=float(input("Enter CIB: "))
    Ci=float(input("Enter Citibank: "))
    A=float(input("Enter AAIB: "))
    Am=350000
    Eu=200000
    St=50000
    ypy=6000*12
    spy=(20000*12)+200000
    fm,fd=Feloos(C,Ci,A)
    fpy,fps=So7abak(fm,ypy,spy)
    Wi=Whatif(Am,Eu,St,fm)
    print("Feloosak Masry: ",fm , "Feloosak Dollar: ",fd)
    print("Youssef should work",fpy, "years to make Fady's money and Safi should work",fps, "years to make Fady's money")
    yn=int(input("Would you like to see your money in CAD? Enter: 1 if yes and 0 if no "))
    if yn==1:
        print(fm/11)
    else:
        print("OK")
    
    print("if Fady didn't go to the US and Europe, Youssef should work",(Wi/ypy),"years to make Fady's money and Safi should work", (Wi/spy), "years to make Fady's money")
    
if __name__ == "__main__":
    main()



