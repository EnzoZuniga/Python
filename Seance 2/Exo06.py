jour = int(input("Entrez la date du jour d'aujourd'hui :"))
mois = int(input("Entrez le numéro du mois :"))
année = int(input("Entrez l'année actuel :"))
février = 0
moisTrenteetun=[1,3,5,7,8,10,12]
moisTrente=[4,6,9,11]

if année%400==0 or (année%4==0 and année%100!=0):
    février = 29
    print("L'année ",année," est une année bisextile.")
else :
    février = 28
    print("L'année ",année," n'est pas une année bisextile.")

if mois == 2:
    if jour == 28:
        mois=mois+1
        jour=1
        print("Demain nous serons le :",jour,"/",mois,"/",année)
    elif jour == 29:
        mois=mois+1
        jour=1
        print("Demain nous serons le :",jour,"/",mois,"/",année)
    else:
        jour=jour+1

if mois in moisTrenteetun and jour==31:
    jour = 1
    if mois == 12:
        mois = 1
        année = année+1
        print("Demain nous serons le : ",jour,"/",mois,"/",année)
    else:
        mois = mois+1
        print("Demain nous serons le :",jour,"/",mois,"/",année)

elif mois in moisTrente and jour==30:
    jour=1
    mois=mois+1
    print("Demain nous serons le :",jour,"/",mois,"/",année)

else:
    jour=jour+1
    print("Demain nous serons le :",jour,"/",mois,"/",année)
