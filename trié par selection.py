from random import*
n=int(input("Nombre d'éléments à trier"))
liste_initial=[randrange(100) for k in range (n)]
compt=0

print(liste_initial)

for k in range (n-1,0,-1):
    compt+=1
    m=max(liste_initial[:k+1])
    i= liste_initial.index(m)
    liste_initial[k], liste_initial[i]=liste_initial[i], liste_initial[k]
    print("Après", compt,"tris par selection:")
    print(liste_initial)

print("Liste triée par sélection :")
print(liste_initial)
