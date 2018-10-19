nombre=float(input("Entrez un Nombre entre 0 et 20: "))
if 0<=nombre<=20 :
    if nombre <8:
        print("Ajourné")
    elif 8 <= nombre < 10 :
        print("Oral de rattrapage.")
    else:
        print("Admis")
else :
    print("Votre nombre n'est pas compris entre 0 et 20")
