def Feloos(C,Ci,A):
    fm=C+(Ci*16)+A
    fd=fm/16
    return fm,fd
    
def So7abak(fm,ypy,spy):
    fpy=fm/ypy
    fps=fm/spy
    return fpy,fps
    
def Potential(fm):
    sal=8*15000
    pot=fm+sal
    exp=100000+(27815*7)
    fin=pot-exp
    return fin

def Post(fin):
    post=fin+260000
    return post

def Whatif(Am,Eu,St,fm):
    Wi=(Am+Eu+St)+fm
    return Wi
    
def main():
    print("\033[1;32;40m Feloos Fady  \n")
    C=float(input("Enter CIB: "))
    Ci=float(input("\nEnter Citibank: "))
    A=float(input("\nEnter AAIB: "))
    Am=350000
    Eu=200000
    St=50000
    ypy=6000*12
    spy=(20000*12)+200000
    fm,fd=Feloos(C,Ci,A)
    fpy,fps=So7abak(fm,ypy,spy)
    Wi=Whatif(Am,Eu,St,fm)
    fin=Potential(fm)
    post=Post(fin)
    print("\033[1;31;40m")
    print("Feloosak Masry: ",round(fm) , "\nFeloosak Dollar: ",round(fd), "\nWorst Case 2020: ",round(fin), "\nVancouver: ",round(post))
    print("\033[1;33;40m")
    print("\nYoussef should work",round(fpy), "years to make Fady's money and \nSafi should work",round(fps), "years to make Fady's money")
    print("\033[1;31;40m")
    yn=int(input("\nWould you like to see your money in CAD? Enter: 1 if yes and 0 if no "))
    if yn==1:
        print("Your money in CAD is= ",(round(fm/11)))
    else:
        print("OK")
    print("\033[1;32;40m")
    print("if Fady didn't go to the US and Europe, \nYoussef should work",round(Wi/ypy),"years to make Fady's money and \nSafi should work", round(Wi/spy), "years to make Fady's money")
    
if __name__ == "__main__":
    main()






