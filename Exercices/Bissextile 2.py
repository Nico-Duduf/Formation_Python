# -*-coding:Latin-1 -*

# Une année est dite bissextile si elle est un multiple de 4,
# SAUF si elle est un multiple de 100.
# Toutefois, elle est bissextile si elle est un multiple de 400.

# Demander l'année
annee = raw_input("Quelle année veux-tu tester, cher utilisateur ?\n")
# Convertir la chaine en integer
annee = int(annee)
# La variable du résultat
bissextile = False


# si (multiple de 4 et pas multiple de 100) ou multiple de 400
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    # bissextile
    bissextile = True
# sinon
else:
    #on n'est pas
    bissextile = False


# Afficher le résultat
if bissextile:
    print(str(annee) + " est bissextile !")
else:
    print("Pas d'bol, " + str(annee) + " n'est pas bissextile !")
