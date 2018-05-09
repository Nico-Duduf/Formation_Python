#demander du texte
texte = raw_input("Du texte ?\n")

resultat = ""

#pour chaque caractere
for carac in texte:
    #si voyelle, *
    if carac in "aeiouyAEIOUY":
        resultat = resultat + "*"
    #sinon garde le caractere
    else:
        resultat = resultat + carac
    
print(resultat)
