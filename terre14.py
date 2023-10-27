# Déterminer si une liste d'entiers est triée ou non

import sys

def trieoupas(lst_entiers):
    for x in range(len(lst_entiers)-1):
        if lst_entiers[x] < lst_entiers[x+1]:
            return True
        return False

try:
    
    if len(sys.argv) < 3:
        print("Saisir au moins 2 entiers")
    else:
        i = [int(arg) for arg in sys.argv[1:]]
        if trieoupas(i) == True:
            print("Triée")
        else:
            print("Pas triée")

except:
    print("Rentrer une liste de nombre entier")