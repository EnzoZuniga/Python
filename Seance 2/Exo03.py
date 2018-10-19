dommage=float(input("Entgrez le montant de vos dommage : "))
franchise = 0.1
MontantFranchise = dommage * franchise

if MontantFranchise < 15 :
    print("Vous avez à votre charge 15 euros.")
elif MontantFranchise > 500 :
    print("Vous avez à votre charge 500 euros.")
else :
    print("Vous avez à votre charge : ",MontantFranchise," euros.") 

print("Vous êtes remboursé ",dommage-MontantFranchise," euros.")
