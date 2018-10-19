
alphb ='ABCDEF'
n, hex = int( input("Entrez le nombre décimal à convertir :"))
while n:
    if (n%16) >= 10:
        hex alphb [(n%16)%10] + hex
    else:
        hex = str (n%16) + hex
    n=n//16

print("L'écriture hexaecimal du nombre saisi est : ", hex)
