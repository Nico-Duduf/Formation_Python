from random import choice

# mode deboggage
is_debug = True;
def debug(message):
    if is_debug:
        print("DEBUG::: " + str(message))




# liste de mots
les_mots = ["Shawarma","Falafel","Burritos","Waterzooie"]
continuer = True

# tant que on continue à jouer
while continuer:
    # DEBUG
    debug("debut du cycle de jeu")
        
    # initialisation :
    # on met le score à 10
    score = 10
    # choisir un mot au hasard
    le_mot = choice(les_mots)
    # le convertir en majuscules
    le_mot = le_mot.upper()
    # liste des lettres trouvées
    les_trouvailles = ""
    # liste des lettres fausses demandées
    les_erreurs = ""
    # liste des lettres demandées
    les_lettres = ""

    # DEBUG
    debug(le_mot)

    gagne = False
    perdu = False

    # tant que il a pas gagné ou il a plus de 0
    while not gagne and not perdu:

        # DEBUG
        debug("debut du cycle choix de mot")
        debug(score)

        # affichage sympa
        print("Nombre d'essais restant : " + str(score))
        print("Lettres déjà demandées : " + les_lettres)
        
        # afficher le mot avec des tirets pour toutes les lettres pas encotre trouvées
        affiche = ""
        for caractere in le_mot:
            if caractere in les_lettres:
                affiche = affiche + caractere
            else:
                affiche = affiche + "-"
        print("Voici le mot à trouver : " + affiche)

        # si toutes les lettres sont trouvées
        if not ("-" in affiche):  
            # gagné
            gagne = True
            break
        
        # demande une lettre
        lettre_joueur = raw_input("Choisis une lettre !\n")
        lettre_joueur = lettre_joueur.upper()
        # utilsateur choisit une lettre

        # si il en demande plusieurs ce gros con
        if len(lettre_joueur) > 1:
            print("Une seule, gros con !")
            continue

        # si il en demande aucune ce débile
        if len(lettre_joueur) == 0:
            print("On t'a demandé une lettre, abrutti!")
            continue

        # si la lettre a déjà été demandée
        if lettre_joueur in les_lettres:
            print("Espèce de gros con, tu as déjà demandé cette lettre !")
            continue

        # ajouter à la liste des lettres demandées
        les_lettres = les_lettres + lettre_joueur
        # trier la liste
        les_lettres = sorted(les_lettres)
        les_lettres = ''.join(les_lettres)
        
        # si elle est dans le mot
        if lettre_joueur in le_mot:
            # on dit bravo
            print("Youhou !")
        # sinon
        else:
            # on diminue le score de 1
            score = score - 1
            debug(score)
            # si le score est à 0
            if score == 0:
                # perdu
                perdu = True

    # si gagné
    if gagne:
        # bravo
        print("Bravo !")
    # sinon
    else:
        # gros nul
        print("Gros naze!")

    # continuer ?
    reponse = raw_input("Veux tu continuer à jouer ? [O/N]\n")
    if reponse in "Nn":
        continuer = False
        
# au revoir
print("Bye bye !")
