# Défi #2
#
# Écrivez un programme qui trouve tous les nombres parfaits inférieurs à
# 10,000. Un nombre parfait est un nombre entier positif qui est égal à
# la somme de ses diviseurs propres (excluant le nombre lui-même).
import math


def nb_parfait(nb: int) -> bool:
    # Pour trouver les diviseurs, on arrête à racine de n
    max = int(math.sqrt(nb)) + 1
    sum = 0

    # Le 1 est inclus dans ce problème
    for i in range(1, max):

        # Tous les diviseurs
        if nb % i == 0:

            # On additionne le diviseur
            sum += i

            # On additionne aussi le 2e diviseur correspondant.
            # Par exemple si nb = 6 et que i = 2, on a trouvé les diviseurs 2 et 3
            # Par contre on n'additionne pas le nombre lui-même lorsque i = 1
            if 1 < i < max:
                sum += nb // i

        # On arrête la boucle si la somme est plus grande que le nombre
        # Ce n'est pas un nombre parfait on arrête de chercher
        if sum > nb:
            break

    return nb == sum

MAX = 10_000
for nb in range(3, MAX):
    if nb_parfait(nb):
        print(nb)