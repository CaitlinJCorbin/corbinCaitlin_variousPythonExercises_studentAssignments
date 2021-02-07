#Caitlin J. Corbin
#Intro to Python
#Draw a Clock
#June 15, 2020

import turtle

turtle.pensize(3)    #minutes
turtle.forward(180)
turtle.right(180)
turtle.forward(180)

turtle.pensize(2)    #seconds
turtle.right(90)
turtle.forward(200)
turtle.right(180)
turtle.forward(200)

turtle.pensize(4)    #hours
turtle.right(195/2)
turtle.forward(140)
turtle.right(180)
turtle.forward(140)

turtle.left(90/12)   #draws the outer portion of the clock
turtle.penup()
turtle.forward(240)
turtle.left(90)
turtle.pendown()
turtle.pensize(3)
turtle.circle(240)