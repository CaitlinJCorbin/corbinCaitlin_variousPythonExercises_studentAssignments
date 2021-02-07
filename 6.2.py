'''
Caitlin J. Corbin
Intro to Python
6.2
6/22/2020
'''
#calculates sum
def sumDigits(num):
    if(num <= 9):
        return num
    else:
        return (num % 10) + sumDigits(num // 10)
#User input
def main():
    n = eval(input("Enter an integer: "))
    print("The sum of the digits in " ,n, "is", sumDigits(n))
#calls main function
main()