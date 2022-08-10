import turtle
n = 150
m = 200

anh_screen = turtle.Screen()

cay_but = turtle.Turtle()
cay_but.pensize(5)
cay_but.pencolor("red")
cay_but.fillcolor("blue")
cay_but.begin_fill()

# Ve hinh chu nhat
turtle.forward(n)
turtle.left(90)
turtle.forward(m)
turtle.left(90)
turtle.forward(n)
turtle.left(90)
turtle.forward(m)
turtle.left(90)
cay_but.end_fill()

turtle.done()
