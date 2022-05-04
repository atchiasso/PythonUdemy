def recuperer_infos_personne(numero):
    nom = input("Nom de la personne " + str(numero) + ": ")
    age = input("Age de la personne " + str(numero) + ": ")
    return nom, age

def afficher_infos_personne(numero, nom, age):
    print("La personne", numero, "est", nom, "son age est", age, "ans")
    print("Le nom possède", len(nom), "caractères")

def recuperer_et_afficher_infos_programme(numero):
    nom, age = recuperer_infos_personne(numero)
    afficher_infos_personne(numero, nom, age)

nb_personnes = 3

for i in range(nb_personnes):
    recuperer_et_afficher_infos_programme(i+1)
