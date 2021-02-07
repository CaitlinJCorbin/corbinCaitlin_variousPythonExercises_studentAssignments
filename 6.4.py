'''
Caitlin J. Corbin
Intro to Python
6.4
6/22/2020
'''
#reverses int
def reverse(num):
    for x in range(len(str(num))):
        y = num % 10
        print(y, end = "")
        num = num // 10
#prints result to user
def main():
    x = int(input("Enter integer: "))
    return print(str(reverse(x)))
#calls main
if __name__ == '__main__':main()