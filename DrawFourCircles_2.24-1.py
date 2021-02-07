#Caitlin J. Corbin
#Intro to Python
#Draw Four Circles
#June 15, 2020
#give the drawing ability
import turtle
#user prompt
r = eval(input("Enter radius: "))
#first position
turtle.penup()
turtle.forward(r)
#draws top right circle
turtle.pendown()
turtle.circle(r)
#draws bottom right circle
turtle.right(180)
turtle.circle(r)
#position switch
turtle.penup()
turtle.forward(2*r)
#draws bottom left circle
turtle.pendown()
turtle.circle(r)
#draws top left circle
turtle.right(180)
turtle.circle(r)
#end
turtle.done