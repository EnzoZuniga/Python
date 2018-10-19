print('Dans cette algorithme, la première variable prendra la valeur de la troisième variable, et la deuxième de la quatrème.')
a=int(input('Entrez la valeur de votre première variable :'))
b=int(input('Entrez la valeur de votre seconde variable :'))
c=int(input('Entrez la valeur de votre troisième variable :'))
d=int(input('Entrez la valeur de votre quatrième variable :'))
a, b, c, d = c, d, a, b
print('Première variable=',a,'Deuxième variable=',b,'Troisime variable=',c,'Quatrième variable=',d)
            
