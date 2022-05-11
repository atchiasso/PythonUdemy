#def tri_personnalise(e):
    # tri par la longueur des strings
#    return len(e)

def afficher(collection, n=-1):
    #collection.sort(key=tri_personnalise)
    c = collection
    if n != -1:
        c = collection[0:n]
    if len(c) == 0:
        print("AUCUNE PIZZA")
        return

    print(f"---- LISTE DES PIZZAS ({len(c)}) ----")
    for i in range(len(c)):
        print("  ", c[i])
    print("Première pizza : ", c[0])
    print("Dernière pizza : ", c[-1])

def ajouter_pizza_utilisateur(collection):
    reponse = input("Pizza à ajouter : ")
    if reponse.lower() in collection:
        print("ERREUR : la pizza existe déjà")
    else:
        collection.append(reponse)

pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
#vide = ()

ajouter_pizza_utilisateur(pizzas)
afficher(pizzas, 2)