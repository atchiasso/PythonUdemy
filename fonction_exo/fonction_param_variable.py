def somme(titre, **nombres):
    print("TITRE :", titre)
    resultat = 0
    for n in nombres:
        resultat += n
    return resultat

print(somme("somme des notes",5,2,4,7,8))