'''
Name: Caitlin J. Corbin
Class: Intro to Python
Name of the assignment: Replace Text
Due date of the assignment: July 13, 2020
'''
# User enters filename, and string is switched
filename = input('Enter a filename: ')
find_string = input('Enter the old string to be replaced: ')
replace_string = input('Enter the new string to replace the old string: ')
lines = []
# Opens file, replaces string
f = open(filename, 'r')
for line in f:
    lines.append(str(line).replace(find_string, replace_string))
f.close()
# Opens & writes to file
w = open(filename, 'w')
for line in lines:
    w.write(line)
w.close()
# Prints done to user
print("Done")

