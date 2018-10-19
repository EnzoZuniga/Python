Mat=[[0,0,0,100,75,50,0],[0,0,100,100,70,40,0],[0,100,100,100,65,35,0],[0,100,0,100,60,30,0],[0,0,0,100,55,25,0],[0,0,0,100,50,20,0]]
compteur=6;
for i in range (0,6):
    for j in range (1,7):
        somme=Mat[i][0]+Mat[i][j];
        Mat[i][0]=somme;
        compteur=compteur+1;
print(somme/compteur);
