# Afficher la valeur du milieu parmis les 3 peramètres données

import sys

def nb_mid (entiers):
    a = int(entiers[0])
    b = int(entiers[1])
    c = int(entiers[2])
    if a == b or a == c or b == c:
        print("Saisir 3 entiers différents")
    else:
        entiers.clear()
        entiers.append(a)
        entiers.append(b)
        entiers.append(c)
        entiers.remove(max(entiers))
        entiers.remove(min(entiers))
        print(entiers[0])
        
try:
    x = list(sys.argv[1:])
    if len(x) != 3:
        print("Rentrer 3 nombres entier")
    else:
        nb_mid(x)
except:
    print("Rentrer 3 nombres entier")