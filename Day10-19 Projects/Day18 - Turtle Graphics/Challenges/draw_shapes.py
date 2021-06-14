from turtle import Turtle, Screen
import random
'''
dış açılar toplamı 360
bir dış açı 360/kenar sayısı
bir iç açı 180 - bir dış açı'''

colors = ["red", "cornflower blue", "medium turquoise", "dark orange", "hot pink", "dark orchid", "lawn green",
          "medium spring green", "midnight blue"]


def external_angle(edge):
    return 360/edge


def shape(t, edge, length):
    for _ in range(edge):
        t.forward(length)
        t.right(external_angle(edge))


def main():
    t = Turtle()
    screen = Screen()

    for i in range(3, 10, 1):
        t.color(random.choice(colors))
        shape(t, i, 100)

    screen.exitonclick()


main()