import turtle

def square():
    for f in range(4):
        turtle.forward(20)
        turtle.right(90)

while True:
    square()
    turtle.penup()
    turtle.forward(40) 
    turtle.pendown()
