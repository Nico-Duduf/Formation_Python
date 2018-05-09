is_debug = True;

# une fonction simple
def power(nombre,puissance):
    i = 0
    resultat = 1
    while i < puissance:
        resultat = resultat*nombre
        i = i+1
    return resultat

# une fonction qui retourne plusieurs résultats
def decomposer(nombre,divise_par):
    """Retourne le résultat de la division entière
    ainsi que le reste.
    Oui ça sert à rien."""
    reste = nombre % divise_par
    resultat_entier = nombre // divise_par
    return resultat_entier, reste
    
# une autre fonction simple qui utilise une variable créée en dehors
def debug(message):
    if is_debug:
        print("DEBUG::: " + str(message))

# une fonction lambda
addition_lambda = lambda a,b: a+b
# est exactement la meme chose que :
def addition(a,b):
    return a+b

mon_resultat = power(2,3)
debug(mon_resultat)
print(mon_resultat)

le_resultat_entier, le_reste = decomposer(12,5)
debug(le_reste)
print(le_resultat_entier)

l_addition_SVP = addition(3,2)
print(l_addition_SVP)
l_addition_SVP_lambda = addition_lambda(6,3)
print(l_addition_SVP_lambda)
