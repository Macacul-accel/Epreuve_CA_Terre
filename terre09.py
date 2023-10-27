# Afficher la racine carrée du nombre entier

import sys

try:
    x = int(sys.argv[1])
    if len(sys.argv) == 2:
        if x < 0:
            print("Ne pas rentrer de nombre négatif")
        else:
            r = x ** 0.5
            print(int(r))
    else:
        print("Vous avez rentrer trop d'arguments")

except:
    print("Veuillez rentrer UN nombre entier positif")