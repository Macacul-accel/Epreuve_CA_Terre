# Afficher pair ou impair selon l'entier entré

import sys

try:
    if len(sys.argv) > 2:
        print("Ne rentrer qu'un seul argument")
    else:
        x = int(sys.argv[1])
        if x % 2 == 0:
            print('Pair')
        elif x % 2 != 0:
            print('Impair')
except:
    print("Rentrez un chiffre")
