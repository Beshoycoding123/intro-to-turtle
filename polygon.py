import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
sides=6
length=70
angle=360/sides
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()