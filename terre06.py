# Afficher l'inverse de la chaine donnée en argument

import sys

try:
    x = sys.argv[1]  
    if len(sys.argv) > 2:
        print("Ne rentrer qu'une chaîne")  
    else:
        if len(x) > 1:
            print(x[::-1])
except:
    print("Veuillez rentrer un argument")
