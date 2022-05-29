noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# 1 - for / len (Méthode qui prend le - de mémoire)
'''nbr = 0
for i in noms:
    nbr += len(i)
print(nbr)'''

# 2 - Completion de liste + sum (Méthode qui prend le + de mémoire)
'''longueur_noms = [len(i) for i in noms]
print("Nombre total de caractères:", sum(longueur_noms))'''

# 3 - Join / len (Methode la plus pratique)
tous_les_noms = "".join(noms)
print("Nombre total de caractères:", len(tous_les_noms))