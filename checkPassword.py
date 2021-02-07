'''
Name: Caitlin J. Corbin
Class: Intro to Python
Name of the assignment: checks password
Due date of the assignment: June 21, 2020
'''
#prompt
password = str(input("Enter an 8 digit password [No special characters - only letters/numbers: "))
#selection structure
def get_digits(password):
    return [i for i in password if i.isdigit()]

#sets a variable
numbers = ''.join(get_digits(password))
#selection structure to determine proper user output
if (len(password) < 8) or (len(numbers) < 2):
    print(password, "is an invalid password")
else:
    print(password, "is a valid password")