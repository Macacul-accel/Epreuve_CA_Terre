# Afficher si un nombre est premier ou non

import sys

def nbprem(x):
    i = 2
    while x % i != 0:
        i += 1
        if x == i:
            print(f"{x} est un nombre premier")
            break
    else:
        print(f"{x} n'est pas un nombre premier")

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
            nbprem(x)

except:
    print("Rentrer un nombre")
