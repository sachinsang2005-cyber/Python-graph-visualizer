import turtle
import math
import numpy as np

a = turtle.Turtle()
a.speed(0)
a.hideturtle()

# draw axes
a.forward(400)
a.backward(800)
a.home()
a.left(90)
a.forward(400)
a.backward(800)
a.home()
a.right(90)


def trigo():
    fun = input("Enter the trignometric function you want to plot (sinx, cosx, tanx): ")
    a.penup()
    a.home()
    a.pendown()
    for x in np.arange(0, 721, 1):
        rad = math.radians(x)   
        if fun == "sinx":
            a.goto(x * 0.5, math.sin(rad) * 100)
        elif fun == "cosx":
            a.goto(x * 0.5 , math.cos(rad) * 100)
        elif fun == "tanx":
            a.goto(x * 0.5, math.tan(rad) * 100) 
   
    return a


def line():
    m = float(input("Enter the slope (m): "))
    c = float(input("Enter the y-intercept (c): "))
    a.penup()

    # move to first point WITHOUT drawing
    x = -400
    y = (x**2) / (4 * c)
    a.goto(x, y)

    a.pendown()
    
    for x in range(-400, 401):
        y = m * x + c
        a.goto(x, y)
    
    return a

def circle():
    r = float(input("Enter the radius of the circle: "))
    for angle in range(0, 361):
        rad = math.radians(angle)
        x = r * math.cos(rad)
        y = r * math.sin(rad)
        a.goto(x, y)
        
    return a


def ellipse():
    a_axis = float(input("Enter the length of the semi-major axis (a): "))
    b_axis = float(input("Enter the length of the semi-minor axis (b): "))
    for angle in range(0, 361):
        rad = math.radians(angle)
        x = a_axis * math.cos(rad)
        y = b_axis * math.sin(rad)
        a.goto(x, y)
        
    return a

def parabola():
   
    p = float(input("Enter the distance from vertex to focus (p): "))
    a.penup()
    x = -200
    y = (x**2) / (4 * p)
    a.goto(x, y)

    a.pendown()
   
   
    for x in range(-200, 201):
        y = (x**2) / (4 * p)
        a.goto(x, y)
    return a    

print("1.trignometric functions")
print("2.straight lines")
print("3.circles")
print("4.ellipses")
print("5.parabolas")



stop = ''
while (stop != 'y'):
    fun = int(input("Enter the type of graph you want to plot (1-5): "))
    if fun == 1:
        trigo()
    elif fun == 2:
        line()
    elif fun == 3:
        circle()
    elif fun == 4:
        ellipse()
    elif fun == 5:
        parabola()
    stop = input("Do you want to stop? (y/n): ")


