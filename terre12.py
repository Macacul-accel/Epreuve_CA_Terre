# Afficher l'heure dans un format de 24 heures

import sys

try:
    x = sys.argv[1]
    hrs = int(x[:2])
    mns = int(x[3:5])
    APM = x[5:]

    if not hrs in range(1, 13):
        print("Dans ce format les heures sont comprises entre 1 et 12")
    elif not mns in range(0, 60):
        print("Les minutes sont comprises entre 0 et 59")
    else:
        if hrs == 12:
            if APM.upper() == "PM":
                print(f"00:{mns}")
            else:
                print(f"{hrs}:{mns}")
        elif APM.upper() == "AM":
            print(f"{hrs}:{mns}")
        else:
            print(f"{hrs + 12}:{mns}")

except:
    print("Rentrer un format 'heure:minuteAM/PM'")