import turtle

anh_screen = turtle.Screen()

#Tạo cây bút vẽ
cay_but = turtle.Turtle()
cay_but.pensize(5)

#Tô màu viền và trong của hình tròn
cay_but.pencolor("red")
cay_but.fillcolor("blue")
cay_but.begin_fill()

#Vẽ hình tròn
cay_but.circle(100)
cay_but.end_fill()



turtle.done()