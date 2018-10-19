phrase = input("Entrez une phrase : ")
caractere =input("Quelle lettre vous cherchez :")
nombre =0
for lettre in phrase:
    if lettre == caractere:
        nombre +=1

print ("Il y a ",nombre," fois la lettre ",caractere," dans votre phrase.")
