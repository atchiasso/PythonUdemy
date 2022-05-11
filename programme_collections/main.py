# Collections : (Tableaux : Array), Listes, Tuples
# Tuple : immutable -> Non modifiable
# Liste []: mutable -> modifiable
# slice : [start:stop:step] -> start inclusif / stop exclusif

noms = []

while(True):
    nom = input("Nom de la personne : ")
    if nom == "":
        break
    print("Le nom est : ", nom)
    noms.append(nom)

print(noms)