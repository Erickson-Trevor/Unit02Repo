import turtle

Global_Scale_1 = 4
Global_Scale_2 = 3
Global_Scale_3 = 2
Global_Angle_1 = 70
Global_Angle_2 = 35
Global_Angle_3 = 0
Global_Line_Color_1 = "red"
Global_Line_Color_2 = "navy"
Global_Line_Color_3 = "darkorchid"
Global_Fill_Color_1 = "tomato"
Global_Fill_Color_2 = "steelblue"
Global_Fill_Color_3 = "violet"
turtle_background_color = "pink"

def paramaters():
    Global_Scale_1 = input("Box Scale 1: ")
    Global_Scale_2 = input("Box Scale 2: ")
    Global_Scale_3 = input("Box Scale 3: ")
    Global_Angle_1 = input("Box Angle: ")


def turtlemovement(a,b,c,d):
    turtle.pencolor(c)
    turtle.fillcolor(d)
    turtle.begin_fill()
    turtle.left(b)
    turtle.forward(a*50)
    turtle.left(90)
    turtle.forward (a*50)
    turtle.left(90)
    turtle.forward(a*50)    
    turtle.left(90)
    turtle.forward(a*50)
    turtle.end_fill()
    turtle.home()

def main(a,b,c,d,e,f,g,h,i,j,k,l):
    #paramaters()
    turtle.bgcolor(turtle_background_color)
    turtlemovement(a,d,g,j)
    turtlemovement(b,e,h,k)
    turtlemovement(c,f,i,l)
    input("Waiting for input")

main(Global_Scale_1,
Global_Scale_2,
Global_Scale_3,
Global_Angle_1,
Global_Angle_2,
Global_Angle_3,
Global_Line_Color_1,
Global_Line_Color_2,
Global_Line_Color_3,
Global_Fill_Color_1,
Global_Fill_Color_2,
Global_Fill_Color_3)

