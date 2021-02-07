'''
Name: Caitlin J. Corbin
Class: Intro to Python
Name of the assignment: 13.2
Due date of the assignment: July 13, 2020
'''
# Main function
def main():
    while True:
        try:
            # Allows user to create a file
            filename = input("Enter a filename: ").strip()
            infile = open(filename, "r")
            break
            # Error message
        except IOError:
            print("File " + filename + " does not exist. Try again.")

    # Finds length
    charCount, wordCount, lineCount = 0, 0, 0
    for line in infile:
        charCount += len(line)
        lineCount += 1
        listOfWords = line.split()
        wordCount += len(listOfWords)

    # Prints data to user
    print(charCount, " characters")
    print(wordCount, " words")
    print(lineCount, " lines")

    # Close file
    infile.close()

# Calls main
main()