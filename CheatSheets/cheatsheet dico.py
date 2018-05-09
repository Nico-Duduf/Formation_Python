unDicoVide = {}
unDico = {"Nom":"Duduf", "Prénom":"Nicolas","Age":25 }

unDico["Prénom"] = "Bertrand"

reponse = "Bonjour {0} {1}, qui a {2} ans"
reponse = reponse.format(unDico["Prénom"],unDico["Nom"],str(unDico["Age"]))
print(reponse)

