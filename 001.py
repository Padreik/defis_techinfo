# Défi #1
#
# Les facteurs premiers de 13195 sont 5, 7, 13 et 29.
# Quel est le plus grand facteur premier de 600851475143.
# Réponse: 6857

import math


# Fonction qui retourne True si le nombre reçu est premier
def est_premier(nb):
    # On commence à True, on mettera à False si on trouve un diviseur
    premier = True
    # On test tous les nombres impairs dans la boucle
    i = 3
    # En vérifiant de 2 à racine de nb, on couvre toutes les possibilités
    max = math.sqrt(nb)

    # On essaie de voir s'il est divisible par 2, le seul nombre premier et pair
    if nb % 2 == 0:
        premier = False

    # On test tous les nombres impairs
    while i <= max and premier:
        if nb % i == 0:
            premier = False
        i += 2
    return premier


# Trouve le plus grand facteur premier pour un nombre donné
def plus_grand_facteur(nb):
    # Facteur 0 tant qu'un facteur plus grand n'est pas trouvé
    facteur = 0

    # On va diviser par tous les nombres, a partir de 2
    i = 2

    # On arrête de vérifier à la racine de nb
    limit = math.sqrt(nb)

    while i < limit:

        # Si nb est divisible par i, on a trouvé un diviseur
        if nb % i == 0:
            tmpFacteur = nb // i

            # S'il est premier, on garde le facteur qu'on vient de trouver
            # sinon, on trouve son plus grand facteur à ce diviseur
            tmpFacteur = tmpFacteur if est_premier(tmpFacteur) else plus_grand_facteur(tmpFacteur)

            # On garde le plus grand facteur entre le nouveau et l'ancien facteur en mémoire
            facteur = max(tmpFacteur, facteur)
        i += 1

    # Si facteur est encore à zéro (donc aucun trouvé), on donne nb, sinon on donne le facteur
    return facteur if facteur else nb


print(plus_grand_facteur(600851475143))
