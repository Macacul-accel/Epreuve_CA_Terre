# Afficher l'heure en format 12 heures

import sys

try:
    x = sys.argv[1]
    hrs = int(x[:2])
    mns = int(x[3:])

    if hrs > 23 or hrs < 0:
        print("Saisir une heure entre 0 et 23")
    elif mns > 59 or mns < 0:
        print("Les minutes sont comprises entre 0 et 59")
    else:
        if hrs == 12:
            print(f"{hrs}:{mns}PM")
        elif hrs == 0:
            print(f"12:{mns}AM")
        elif hrs < 12:
            print(f"{hrs}:{mns}AM")
        else:
            print(f"{hrs-12}:{mns}PM")
            
except:
    print("Rentrer un format 'heure:minute'")