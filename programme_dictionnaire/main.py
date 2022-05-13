# --- PARTIE 1 ---
"""personne = {"nom": "Mélanie", "age": 25, "taille": 1.60}

achat = ("Chocolat", "beurre", "fromage")
personne["achat"] = achat
print(personne["achat"][0])"""

# --- PARTIE 2 ---

personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65)
]

def obtenir_informations(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

infos = obtenir_informations("Jacques", personnes)
# print(infos)

personnes_dict = {
    "Mélanie": (25, 1.6),
    "Paul": (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)
}

infos = personnes_dict.get("Claire")
if not infos:
    print("La clef n'existe pas ")
else:
    print(infos)