'''
Name: Caitlin J. Corbin
Class: Intro to Python
Name of the assignment: Sum of Digits
Due date of the assignment: July 13, 2020
'''
# Function that calculates sum
def sumDigits(n):
    if n < 10:
        return n
    else:
        return sumDigits(n // 10) + n % 10
# Main function, user prompt and displays data
def main():
    num = eval(input("Enter a positive integer: "))
    print("The sum of the digits of: ", num, " is ", sumDigits(num))
# Calls main
main()