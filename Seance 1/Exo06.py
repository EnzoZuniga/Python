print('Dans cette algorithme, la première variable prendra la valeur de la quatrième variable et inversement, la deuxième de la troisième, la troisième de la cinquième et la cinquième de la deuxième.')
a=int(input('Entrez la valeur de votre première variable :'))
b=int(input('Entrez la valeur de votre seconde variable :'))
c=int(input('Entrez la valeur de votre troisième variable :'))
d=int(input('Entrez la valeur de votre quatrième variable :'))
e=int(input('Entrez la valeur de votre cinquième variable :'))
a, b, c, d, e = d, c, e, a, b
print('Première variable=',a,'Deuxième variable=',b,'Troisime variable=',c,'Quatrième variable=',d,'Cinquième variable=',e)
            
