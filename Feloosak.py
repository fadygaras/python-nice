def Feloos(fm):
    fd=fm/16
    return fm,fd
    
def So7abak(fm,ypy,spy):
    fpy=fm/ypy
    fps=fm/spy
    return fpy,fps
    
def main():
    C=float(input("Enter CIB: "))
    Ci=float(input("Enter Citibank: "))
    A=float(input("Enter AAIB: "))
    fm=C+(Ci*16)+A
    ypy=6000*12
    spy=(20000*12)+200000
    fm,fd=Feloos(fm)
    fpy,fps=So7abak(fm,ypy,spy)
    print("Feloosak Masry: ",fm , "Feloosak Dollar: ",fd)
    print("Fady= ",fpy, "Youssef" , "Fady= ",fps, "Safi")
    yn=int(input("Would you like to see your money in CAD? Enter: 1 if yes and 0 if no "))
    if yn==1:
        print(fm/11)
    else:
        print("OK")
    
if __name__ == "__main__":
    main()

