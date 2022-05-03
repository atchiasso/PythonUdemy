import turtle

t = turtle.Turtle()
cpt = 0
#5 marches de 30 pixels
while(cpt != 5):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    cpt += 1
t.forward(30)

turtle.done()
