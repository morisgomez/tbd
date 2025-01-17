#goal: create 2 new files and write information to them from inputFile.txt:


# open inputFile.txt with the intention of reading it
inputFile = open("inputFile.txt", "r")

# open passFile.txt with the intention of writing it
passFile = open("passFile.txt", "w")

# open failFile.txt with the intention of writing it
failFile = open("failFile.txt", "w")
print(inputFile)
# loop through each line in inputFile.txt
for line in inputFile:
    print(line) #each line stores each line of data from txt as a string. Ex: John 32 P
    lineSplit = line.split() #converts each line into a list w/ 3 sub strings. each substring created based on whitespace in line's string. Ex: ['John', '32', 'P']
    print(lineSplit)
    if lineSplit[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)

# close inputFile.txt
inputFile.close()

# close passFile.txt
passFile.close()

# close failFile.txt
failFile.close()
