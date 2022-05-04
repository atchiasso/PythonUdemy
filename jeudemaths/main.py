import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    resultat = input(f"Calculez : {a} + {b} = ")
    resultat_int = int(resultat)
    if resultat_int == (a + b):
        print("Réponse correcte")
    else:
        print("Réponse incorrecte")

for i in range(1, NB_QUESTIONS+1):
    print(f"Question n°{i} sur {NB_QUESTIONS} :")
    poser_question()
    print()