import turtle

anh_screen = turtle.Screen()
facesize = 200
cay_but = turtle.Turtle()
cay_but.pensize(5)
cay_but.pencolor("Blue")
cay_but.fillcolor("green")
cay_but.begin_fill()
#Vẽ hình tròn khuôn mặt
cay_but.penup()
cay_but.goto(0,-200)
cay_but.pendown()
cay_but.circle(100)
cay_but.end_fill()

#Vẽ đôi mắt
eyesize = 20
cay_but.pensize(2)
cay_but.pencolor("black")
cay_but.fillcolor("red")
cay_but.penup()
cay_but.goto(50,-70)
cay_but.pendown()
cay_but.begin_fill()
cay_but.circle(eyesize)
cay_but.end_fill()


cay_but.pencolor("black")
cay_but.fillcolor("yellow")
cay_but.penup()
cay_but.goto(-50,-70)
cay_but.pendown()
cay_but.begin_fill()
cay_but.circle(eyesize)
cay_but.end_fill()

#Vẽ mũi
cay_but.penup()
cay_but.goto(0,-80)
cay_but.fillcolor("orange")
cay_but.pendown()
cay_but.begin_fill()
cay_but.circle(-20,steps=3)
cay_but.end_fill()

#Vẽ miệng
cay_but.penup()
cay_but.goto(-50,-120)
cay_but.pendown()
cay_but.right(90)
cay_but.circle(50,180)

turtle.done()