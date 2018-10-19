n= int(input("Entrez nombre liste"))
liste = n*[1]
for k in range(2,n):
    for i in range (k+1,n):
        if i%k==0:
            liste[i]=0;
        if liste[k] ==0:
            print(k);


