# Afficher le nombre de caractère d'une chaîne

import sys

try:

    try:
        if sys.argv[2]:
            print("Rentrer qu'UNE chaîne")
            
    except:
        x = sys.argv[1]
        if x.isdigit():
            print("Ne pas rentrer de nombres")
        else:
            l = list([ord(i) for i in x])
            nb_car = 0
            while l:
                l.pop(0)
                nb_car += 1
            else:
                print(nb_car)

except:
    print("Veuillez rentrer une chaîne en argument")