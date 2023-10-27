# Afficher si un nombre est premier ou non

import sys

def nbprem(x):
    for i in range(2, x):
        if (x % i) == 0:
            return False
        else:
            return True

try:
    if len(sys.argv) > 2:
        print("Ne rentrer qu'un nombre")
    else:
        x = int(sys.argv[1])
        if x <= 1:
            if x < 0:
                print("Ne pas rentrer de nombre négatif")
            else:
                print(f"{x} n'est pas un nombre premier")
        elif len(sys.argv) > 2:
            print("Ne rentrer qu'une chaîne")
        else:
            if nbprem(x) == False:
                print(f"{x} n'est pas un nombre premier")
            else:
                print(f"{x} est un nombre premier")

except:
    print("Rentrer un nombre")