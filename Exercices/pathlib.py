from pathlib import Path

fileInfo = Path("config_arbo.txt")

le_contenu_du_fichier = ""

with fileInfo.open() as contenu:
    le_contenu_du_fichier = str(contenu.read())


