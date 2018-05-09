# -*-coding:Latin-1 -*

# Demander le nombre
nombre = raw_input("Nombre ?\n")
nombre = int(nombre)

# incrément
i = 0

# tant que l'incrément est inférieur à 10
while i <= 10:
    # calculer et afficher la table
    resultat  = i * nombre
    print(str(nombre) + " x " + str(i) + " = " + str(resultat))
    # incrémenter
    i = i + 1
