from pathlib import Path

def numero(num,nbreCaracteres):
    chaineNum = str(num)
    while len(chaineNum) < nbreCaracteres:
        chaineNum = "0" + chaineNum
    return chaineNum

#Les fonctions
def creeProjet(fichierProjet,cheminProjet):

    separateur = "_"
    
    #ouvrir et charger le contenu du fichier
    with projetFichier.open() as contenu:
        configProjet = str(contenu.read())
        
    #récupérer et lister les infos
    configProjet = configProjet.split("\n")
    idProjet = ""
    nomProjet = ""
    secteurs = []
    nbPlans = 0
    for ligne in configProjet:
        ligne = ligne.split(":")
        clef = ligne[0]
        valeur = ligne[1]
        if clef == "projet":
            valeur = valeur.split("#")
            idProjet = valeur[0]
            nomProjet = valeur[1]
        elif clef == "nombreDePlans":
            nbPlans = int(valeur)
        elif clef == "secteur":
            valeur = valeur.split("#")
            secteur = {"id":valeur[0],"nom":valeur[1]}
    #créer les dossiers
    #dossier au nom du projet
    cheminProjet = cheminProjet + "/" + nomProjet
    dossierProjet = Path(cheminProjet)
    dossierProjet.mkDir()
    # 1 dossier par secteur, id + idProjet + nomSecteur
    for secteur in secteurs:
        nomListe = [ secteur["id"] , idProjet , secteur["nom"] ]
        cheminSecteur = cheminProjet + "/" + separateur.join(nomListe)
        dossierSecteur = Path( cheminSecteur )
        dossierSecteur.mkDir()
        # 1 dossier par plan, idprojet + numéro + secteur
        i = 1
        while i <= nbPlans:
            nomPlan = [ idProjet , numero(i,3) , secteur["nom"] ]
            dossierPlan = Path( cheminSecteur + "/" + separateur.join(nomPlan) )
            dossierPlan.mkDir()
            i = i+1

# Run
cheminProjets = "C:/PROJETS"

#demander le projet
nomProjet = input("Quel est le nom du projet ?\n")
nomProjet = nomProjet.lower()

#le fichier de config
projetFichier = Path(cheminProjets + "/" + nomProjet + ".txt")

#vérifier si le projet existe
if projetFichier.exists():
    creeProjet(projetFichier)
else:
    print("Ce projet n'existe pas, désolé.")
