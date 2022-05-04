import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    resultat = input(f"Calculez : {a} {operateur_str} {b} = ")
    resultat_int = int(resultat)
    calcul = a + b
    if o == 1:
        calcul = a * b
    if resultat_int == calcul:
        return True
    return False

nb_points = 0
moyenne = int(NB_QUESTIONS/2)
for i in range(1, NB_QUESTIONS+1):
    print(f"Question n°{i} sur {NB_QUESTIONS} :")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrecte")
    print()

print()
print(f"Votre note est de {nb_points}/{NB_QUESTIONS}")

if nb_points == NB_QUESTIONS:
    print("Excellent !")
elif nb_points == 0:
    print("Révisez vos maths !")
elif nb_points > moyenne:
    print("Pas mal !")
else:
    print("Peut mieux faire")