phrase = input("Entrez une phrase : ").lower()
nombre =0
listeVoyelle = ['a','e','u','y','o','i']

for lettre in phrase:
    if lettre in listeVoyelle:
        nombre +=1

print ("Il y a ",nombre," voyelle dans votre phrase.")
