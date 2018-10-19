print("Vous allez entrer votre horrair de début.")
heure=int(input("Entrez le nombre d'heures: "))
minute=int(input("Entrez le nombre de minutes: "))
SommeMinute=(heure*60)+minute
print("Vous allez rentrer votre horrair de fin.")
heure2=int(input("Entrez le nombre d'heures: "))
minute2=int(input("Entrez le nombre de minutes: "))
SommeMinute2=(heure2*60)+minute2

diff=SommeMinute2-SommeMinute

if diff > 0:
    heure=diff//60
    minute=diff%60
    print("La durée entre les deux horraires est de ",heure," heure(s) et ",minute," minute(s).")

else:
    print("L'horraire le début est postérieur a l'horraire de fin.")
