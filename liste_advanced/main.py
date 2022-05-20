# LES COLLECTIONS : LISTES / TUPLES
# Append / Extend / += / Insert

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# longueurs_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms]
# nom_avec_e = [nom for nom in noms if "e" in nom]

# a = [i for i in range(5) if (i % 2) == 0]
b = [(i, True if (i%2) == 0 else False) for i in range(5)]
print(b)
