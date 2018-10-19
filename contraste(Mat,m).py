Mat=[[0,0,0,100,75,50,0],[0,0,100,100,70,40,0],[0,100,100,100,65,35,0],[0,100,0,100,60,30,0],[0,0,0,100,55,25,0],[0,0,0,100,50,20,0]]
for i in range (0,6):
    for j in range (1,7):
        somme=Mat[i][0]+Mat[i][j];
        Mat[i][0]=somme;
        compteur=compteur+1;
print(somme/compteur);
moyenne=somme/compteur;

for i in range(0,6):
    for j in range(0,7):
        if Mat[i][j]<moyenne:
            Mat[i][j]=Mat[i][j]/2;
        elif Mat[i][j]>moyenne:
            Mat[i][j]=Mat[i][j]*2;
            if Mat[i][j]>100:
                Mat[i][j]=100;
            else:
                Mat[i][j]=Mat[i][j];
        print(Mat[i])
