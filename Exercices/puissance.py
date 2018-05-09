# -*-coding:Latin-1 -*

# Demander le nombre
nombre = raw_input("Nombre ?")
nombre = int(nombre)
# Demander la puissance
puissance = raw_input("Puissance ?")
puissance = int(puissance)

resultat = 1 # une puissance 0 est égale à un, donc le résultat minimum est 1

i = 0 #incrément pour compter le nombre de fois qu'on a multiplié

# multiplier le résultat par le nombre, autant de fois que la puissance
# tant que on n'a pas fait autant de multiplications que puissance
while i < puissance:
    resultat = resultat * nombre # la multiplication
    i = i + 1 # incrémentation 

# afficher le résultat
print("La puissance " + str(puissance) + " de " + str(nombre) + " est " + str(resultat))
