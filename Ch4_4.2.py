#Gives random ability
import random
#Generates 3 random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
#Calculation
answer = eval(input("What is " + str(num1) + " + "\
+ str(num2) + " + " + str(num3)+ "? "))
#Displays T/F result to user
print(num1, "+", num2, "+", num3, "=", answer,\
"is", num1+num2+num3 == answer)
