n=int(input("Entrer un entier naturel non nul : "))
somme=0

for k in range(n+1):
    if k == n-1:
        print(k)
    elif k!=n+1:
        print(k,"x")
