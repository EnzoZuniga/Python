print('a=c, b=d, c=e, d=a, e=f, f=b')

a=int(input('Entrez la valeur de a :'))
b=int(input('Entrez la valeur de b :'))
c=int(input('Entrez la valeur de c :'))
d=int(input('Entrez la valeur de d :'))
e=int(input('Entrez la valeur de e :'))
f=int(input('Entrez la valeur de f :'))

a,b,c,d,e,f=c,d,e,a,f,b

print('a=',a,'b=',b,'c=',c,'d=',d,'e=',e,'f=',f)
