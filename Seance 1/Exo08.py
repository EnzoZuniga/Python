s=float(input("Entrez votre somme :"))
s=100*s
a=s//50
s=s%50
b=s//20
s=s%20
c=s//10
s=s%10
d=s//5
s=s%5
e=s//2
s=s%2
f=s//1
s=s%1
print("Pour payer la somme, il faut un minimum de :",a+b+c+d+e+f+s,"pièces.")
print(a," pièces de 0.50 euro.")
print(b," pièces de 0.20 euro.")
print(c," pièces de 0.10 euro.")
print(d," pièces de 0.05 euro.")
print(e," pièces de 0.02 euro.")
print(f," pièces de 0.01 euro.")
