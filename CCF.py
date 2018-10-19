n=int(input("Entrez un entier naturel non  nul."))
p=0
u=0
d=0
c=0
liste=[4,16,37,58,89,145,42,20]

def image(n):
    u=n%10
    d ,c = ((n-u)/10)%10 , n//10
    p = u**2+d**2+c**2
    return(int(p))

while p!=100 or p not in liste :
    n = image(n)
    print (p)
    if p==100:
        print("Vous êtes dans le puits...")
    elif p not in liste:
        print("Vous êtes dans le cycle.")


