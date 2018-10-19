nb1=float(input("Entrez une première valeur: "))
nb2=float(input("Entrez une deuxième valeur: "))
nb3=float(input("Entrez une troisième valeur: "))


if nb1 == nb2 == nb3 :
    print("Vous avez deux doublons. Les trois valeurs sont les plus petites.")
    print("La plus petite valeur est donc ",nb1)
    
elif nb1 == nb2 or nb2 == nb3 or nb3 == nb1:
    print("Vous avez un doublons.")
    if nb1==nb2 and nb1< nb3:
        print("La plus petite valeur est ",nb1)
    elif nb2==nb1 and nb2< nb3:
        print("La plus petite valeur est ",nb2)
    else :
        print("La plus petite valeur est ",nb3)
        
else :
    print("Vous n'avez pas de doublons.")
    if nb1<nb2 and nb1< nb3:
        print("La plus petite valeur est ",nb1)
    elif nb2<nb1 and nb2< nb3:
        print("La plus petite valeur est ",nb2)
    else :
        print("La plus petite valeur est ",nb3)
