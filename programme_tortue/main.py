import turtle

def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)
def carres(taille_depart, nb):
    for i in range(0,nb):
        carre((i+1)*taille_depart)

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

t = turtle.Turtle()
#escalier(60,5)
carres(50, 6)
turtle.done()
