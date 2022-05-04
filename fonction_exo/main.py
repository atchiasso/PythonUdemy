def est_majeur(age : int):
    if age <= 0:
        return False
    if age >= 18:
        return True
    return False

def recuperer_infos_personne(numero):
    nom = input("Nom de la personne " + str(numero) + ": ")
    age = input("Age de la personne " + str(numero) + ": ")
    return nom, int(age)

def afficher_infos_personne(numero, nom, age : int):
    print("La personne", numero, "est", nom, "son age est", age, "ans")
    print("Le nom possède", len(nom), "caractères")
    if est_majeur(age):
        print("Il est majeur")
    else:
        print("Il est mineur")

def recuperer_et_afficher_infos_programme(numero):
    nom, age = recuperer_infos_personne(numero)
    afficher_infos_personne(numero, nom, age)

nb_personnes = 3

for i in range(nb_personnes):
    recuperer_et_afficher_infos_programme(i+1)
