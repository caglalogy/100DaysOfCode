import random
import turtle as trt
import colorgram

colors = colorgram.extract('spot_paint.jpg', 40)
colorList = []
for i in range(20):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    color = (r, g, b)
    colorList.append(color)


trt.colormode(255)
trt.bgcolor("white")
t = trt.Turtle()
x = -100
y = -100
for _ in range(8):
    t.penup()
    t.setx(-100)
    t.sety(y)
    t.pendown()
    y += 50
    for i in range(8):
        t.color(random.choice(colorList))
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.penup()
        t.forward(40)
        t.pendown()





