'''
Name: Caitlin J. Corbin
Class: Intro to Python
Name of the assignment: 15.4
Due date of the assignment: July 13, 2020
'''
# Sum function, finds sum at index
def sum(n):
    if n == 1:
        return 1
    else:
        return 1/n + sum(n-1)
# User input/print
index = eval(input("Enter an index: "))
print("The sum at the index: ", index, " is - ", sum(index))