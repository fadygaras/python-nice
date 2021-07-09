def Ma3ayaKam(FeloosCIB,FeloosCitibank,FeloosAAIB):
    feloosMasry=FeloosCIB+(FeloosCitibank*16)+FeloosAAIB
    return feloosMasry,feloosMasry/15.7

def KamSa7eb(feloosMasry,youssefElKhara,safiElFa2eer):
    return feloosMasry/youssefElKhara,feloosMasry/safiElFa2eer

def Mosta2baly(feloosMasry):
    moratab=8*15000
    elAmala=feloosMasry+moratab
    masareef=100000+(27815*7)
    return elAmala-masareef

def GhasseelAmwal(mosta2balyIsA):
    return mosta2balyIsA+260000

def YataraLaw(SarfAmreekani,SarfOroby,NeikaBalady,feloosMasry):
    return SarfAmreekani+SarfOroby+NeikaBalady+feloosMasry

def main():
    print("\033[1;32;40m Feloos Fady  \n")
    feloosCIB=float(input("Enter CIB: "))
    feloosCitiBank=float(input("\nEnter Citibank: "))
    feloosAAIB=float(input("\nEnter AAIB: "))
    sarfAmreekani=350000
    sarfOroby=200000
    neikaBalady=50000
    youssefElKhara=6000*12
    safiElFa2eer=(20000*12)+200000
    feloosMasry,feloosDollar=Ma3ayaKam(feloosCIB,feloosCitiBank,feloosAAIB)
    kamYoussefElKhara,kamSafiElFa2eer=KamSa7eb(feloosMasry,youssefElKhara,safiElFa2eer)
    elForsaElDay3a=YataraLaw(sarfAmreekani,sarfOroby,neikaBalady,feloosMasry)
    mosta2balyInshallah=Mosta2baly(feloosMasry)
    print("\033[1;31;40m")
    print("Feloosak Masry: ",round(feloosMasry) , "\nFeloosak Dollar: ",round(feloosDollar), "\nWorst Case 2020: ",round(mosta2balyInshallah), "\nVancouver: ",round(GhasseelAmwal(mosta2balyInshallah)))
    print("\033[1;33;40m")
    print("\nYoussef should work",round(kamYoussefElKhara), "years to make Fady's money and \nSafi should work",round(kamSafiElFa2eer), "years to make Fady's money")
    print("\033[1;31;40m")
    yn=int(input("\nWould you like to see your money in CAD? Enter: 1 if yes and 0 if no "))
    if yn==1:
        print("Your money in CAD is= ",(round(feloosMasry/12.5)))
    else:
        print("OK")
    print("\033[1;32;40m")
    print("if Fady didn't go to the US and Europe, \nYoussef should work",round(elForsaElDay3a/kamYoussefElKhara),"years to make Fady's money and \nSafi should work", round(elForsaElDay3a/kamSafiElFa2eer), "years to make Fady's money")

if __name__ == "__main__":
    main()

