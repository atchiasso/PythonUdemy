# Collections : (Tableaux : Array), Listes, Tuples
# Tuple : immutable -> Non modifiable
# Liste []: mutable -> modifiable

def obtenir_informations():
    return "Mélanie", 37, 1.68

def afficher_informations(nom, age, taille):
    print(f"Informations: Nom {nom}, age : {age}, taille : {taille}")

infos = obtenir_informations()
afficher_informations(*infos) #unpack tuple