from pathlib import Path

fileInfo = Path("config_arbo.txt")

le_contenu_du_fichier = ""

with fileInfo.open() as contenu:
    le_contenu_du_fichier = str(contenu.read())


print(le_contenu_du_fichier)

la_liste_des_trucs = le_contenu_du_fichier.split("\n")


for ligne in la_liste_des_trucs:
    if ligne.startsWith("projet"):
        nom_du_projet = ligne.split(":")[1]
