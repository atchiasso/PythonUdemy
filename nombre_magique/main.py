import random


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        number = input(f"Quel est le nombre magique ? (entre {nb_min} et {nb_max})  ")
        try:
            nombre_int = int(number)
        except:
            print("Oops! Vous devez rentrer un nombre, réessaye !")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Oops! Le nombre doit être entre {nb_min} et {nb_max}, réessaye !")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)

nombre = 0
while nombre != NOMBRE_MAGIQUE:
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
    else:
        print("Bravo, vous avez gagné !")
