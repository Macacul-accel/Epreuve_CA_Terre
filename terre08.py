# Afficher le résultat d'une puissance

import sys

try:
    x = sys.argv[1]
    y = sys.argv[2]

    if len(sys.argv) > 3:
        print("Ne rentrer que 2 nombres")
    else:
        if x.isdigit() == False or y.isdigit() == False:
            try:
                if int(x) < 0 or int(y) < 0:
                    print("Ne pas rentrer de nombres négatifs")
            except:    
                print("Rentrer que des nombres")
        else:
            i = int(x) ** int(y)
            print(i)

except:
    print("Veuillez rentrer un nombre en 1. et la puissance voulue en 2.")