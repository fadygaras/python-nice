hesabCIB=int(input("Enter the balance of your CIB account: "))
hesabCitibank=int(input("Enter the balance of your Citibank account: "))
hesabAAIB=int(input("Enter the balance of your AAIB account: "))

def FeloosSo7aby():
    # hesab citibank bel dollar yasta
    hesabCitibankMasry=hesabCitibank*15.7
    feloosyMasry=hesabCIB+hesabCitibank+hesabAAIB
    feloosyAmreekany=feloosyMasry/15.7
    feloosyCanady=feloosyMasry/12.5
    moratabYoussef=1*12
    moratabSafi=20000*12
    moratabWahba=135300*0.7*15.7
    # som3a dafe3 darayeb nice
    moratabSom3a=44500*12.5
    # omar by2bad dollar WOO
    moratabOmar=2000*12*15.7
    kamYoussef=feloosyMasry/moratabYoussef
    kamSafi=feloosyMasry/moratabSafi
    kamSom3a=feloosyMasry/moratabSom3a
    kamOmar=feloosyMasry/moratabOmar
    kamWahba=feloosyMasry/moratabWahba
    youssefFilSana=feloosyMasry/moratabYoussef
    safiFilSana=feloosyMasry/moratabSafi
    wahbaFilSana=moratabWahba/feloosyMasry
    print ("Hey Buddy")
    print ("Your money in EGP: ", feloosyMasry)
    print ("Your money in USD: ", feloosyAmreekany)
    print ("Your money in CAD: ", feloosyCanady)
    print ("You have ", kamYoussef, "Youssef")
    print ("You have ", kamSafi, "Safi")
    print ("You have ", kamSom3a, "Ismail")
    print ("You have ", kamOmar, "Omar")
    print ("You have ", kamWahba, "Wahba")
    if youssefFilSana >= 20:
        print("Youssef 3ando Ta2beeda Nice xD")
    print ("Youssef needs to work", youssefFilSana, "years to be equal Fady")
    print ("Safi needs to work", safiFilSana, "years to be equal Fady")
    print ("Wahba per year= ", wahbaFilSana, "Fady")
    print ("Safi needs to work", moratabWahba/moratabSafi, "years to make one Wahba per year")
    if moratabWahba/moratabYoussef >= 1000:
        print("******555555555*********555555******YOUSSEF****GA7SH**********555555555*******GHABY******KHAWAL*******xD")
    print ("Youssef needs to work", moratabWahba/moratabYoussef, "years to make one Wahba per year")
    if moratabWahba/moratabSom3a >= 1000:
        print("******555555555*********SOM3A***KHAYATT******YOUSSEF****GA7SH**********555555555*******GHABY******KHAWAL*******xD")
    print ("Youssef needs to work", moratabWahba/moratabSom3a, "years to make one Ismail per year")
    print ("Youssef needs to work", moratabWahba/moratabOmar, "years to make one Omar per year")


FeloosSo7aby()
