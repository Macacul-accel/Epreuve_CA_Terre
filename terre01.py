# Afficher le nom du fichier en cours

import sys

x = sys.argv[0]
if not "/" in x:
    print(x)
elif "/" in x:
    y = x.split("/")
    print(y[-1])