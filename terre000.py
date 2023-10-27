# Afficher l'alphabet en minuscule + retour à la ligne

for x in map(chr, range(96, 123)):
    print(x, end="")
print("\n")