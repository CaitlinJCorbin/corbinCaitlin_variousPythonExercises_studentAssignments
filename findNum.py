'''
Caitlin J. Corbin
Intro to Python
Finds Numbers
6/22/2020

'''
#uses an iterator and selection structure to calculate findNum
count = 0
for i in range (100, 201):
    if (i % 6 == 0 and i % 5 != 0) or (i % 5 == 0 and i % 6 != 0):
        print(str(i), ""),
        count = count + 1
    if count % 10 == 0:
        print("")