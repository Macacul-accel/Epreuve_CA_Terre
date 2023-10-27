# Afficher l'alphabet à partir d'une lettre donnée + retour à la ligne

import sys

for x in sys.argv[1]:
    for x in range(ord(x), 123):
        print(chr(x),end="")
    print("\n")