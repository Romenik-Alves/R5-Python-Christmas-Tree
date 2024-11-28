from turtle import *
from random import randint
 
 
def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
 
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
 
   # preencha a forma acima
    turtle.end_fill()
    # Redefinir a orientação da tartaruga
    turtle.setheading(0)
 
 
def create_circle(turtle, x, y, radius, color):
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(x, y)
    oogway.pendown()
    oogway.begin_fill()
    oogway.circle(radius)
    oogway.end_fill()
 
 
BG_COLOR = "#0080ff"
 
# "Ontem é história, amanhã é um mistério, mas hoje é um presente. É por isso que é chamado de presente.”
# — Oogway para Po sob o pessegueiro, Kung Fu Panda
oogway = Turtle()
# definir velocidade da tartaruga
oogway.speed(2)
screen = oogway.getscreen()
# definir cor de fundo
screen.bgcolor(BG_COLOR)
# definir bloco de tela
screen.title("Merry Christmas")
# maximizar a tela
screen.setup(width=1.0, height=1.0)
 
y = -100
# criar tronco de árvore
create_rectangle(oogway, "red", -15, y-60, 30, 60)
 
# criar árvore
width = 240
oogway.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(oogway, "green", x, y, width, height)
    y = y + height
 
# crie uma estrela no topo da árvore
oogway.speed(1)
oogway.penup()
oogway.color('yellow')
oogway.goto(-20, y+10)
oogway.begin_fill()
oogway.pendown()
for i in range(5):
    oogway.forward(40)
    oogway.right(144)
oogway.end_fill()
 
tree_height = y + 40
 
# criar lua no céu
# crie um círculo completo
create_circle(oogway, 230, 180, 60, "white")
# sobreponha com o círculo completo da cor BG para fazer uma forma crescente
create_circle(oogway, 220, 180, 60, BG_COLOR)
 
# agora adicione algumas estrelas no céu
oogway.speed(10)
number_of_stars = randint(20,30)
# print(number_of_stars)
for _ in range(0,number_of_stars):
    x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
    y_star = randint(tree_height, screen.window_height()//2)
    size = randint(5,20)
    oogway.penup()
    oogway.color('white')
    oogway.goto(x_star, y_star)
    oogway.begin_fill()
    oogway.pendown()
    for i in range(5):
        oogway.forward(size)
        oogway.right(144)
    oogway.end_fill()
 
# imprimir mensagem de saudação
oogway.speed(1)
oogway.penup()
msg = "Merry Christmas from codehub.py family"
oogway.goto(0, -200)  # y está em menos porque o tronco da árvore estava abaixo do eixo x
oogway.color("white")
oogway.pendown()
oogway.write(msg, move=False, align="center", font=("Arial", 15, "bold"))
 
oogway.hideturtle()
screen.mainloop()