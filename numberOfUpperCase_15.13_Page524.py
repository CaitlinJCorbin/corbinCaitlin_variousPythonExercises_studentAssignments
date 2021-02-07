'''
Name: Caitlin J. Corbin
Class: Intro to Python
Name of the assignment: Number of Upper Case
Due date of the assignment: July 13, 2020
'''
# Function that finds the upper case
def countUppercase(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
            s = s.replace(i, "")
        else:
            s = s.replace(i, "")
            countUppercase(s)
    return count
# User input, prints data to user
element = input("Enter the string: ")
string = countUppercase(element)
print("Number of upper letter in the string: ", string)

# End
