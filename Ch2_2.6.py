number = int(input("Enter a number between 0 and 1000 "))
i = 0
while number > 0:
    digit = number % 10
    i += digit
    number = number // 10
print("The sum of the integer digits: ")
print(i)
