uneListeVide = []
uneListe = ["premiere","deuxieme"]
uneListe.append("troisieme")

autreListe = ["quatrieme","cinquieme"]

uneListe = uneListe + autreListe

for element in uneListe:
    print(element)

for i, element in enumerate(uneListe):
    print("l'élement numéro " + str(i) + " est " + element)

i=0
while i < len(uneListe):
    element = uneListe[i]
    print( element )
    i = i + 1

#le nombre d'éléments dans la liste
len(uneListe)
#le troisième
uneListe[2]
#le dernier
uneListe[-1]

