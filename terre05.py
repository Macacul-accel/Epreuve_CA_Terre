# Afficher le résultat et le reste d'une division entre 2 nombres

import sys

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    if len(sys.argv) > 3:
        print("Ne rentrer que 2 nombres")
    else:    
        if y < x:
            print(f"Le résultat est : {int(x / y)}")
            print(f"Le reste est : {x % y}")
        elif y > x or y == 0:
            print("Erreur")
except:
    print("Erreur")