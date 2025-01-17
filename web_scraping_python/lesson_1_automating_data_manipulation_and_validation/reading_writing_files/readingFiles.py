#exercise 1: read entire file.

#open the file:
inputFile = open("inputFile.txt", "r") #r = to read file.

#reading file's data:
print(inputFile.read())

#closing file after reading:
inputFile.close()

###########
###BREAK###
###########

#exercise 2: read file data ONLY who have passed test.

#open file:
inputFileTwo = open("inputFile.txt", "r")

#create for loop to read only rows who have "P":
for i in inputFileTwo:
    #each row of data/line in the csv is an index "i" starting at 0
    #ex: i[0] is Grace 18 F 
    #i.split() turns each row in csv to a list object.
    # ex: ["Grace", "18", "F"] & Grace is at index 0, 18 at 1 and F at 2
    iSplit = i.split() #["Grace", "18", "F"]
    if(iSplit[2] == "P"): #if the index 2 of list is P, print.
        print(i)

    #summary of for loop logic:
    #in the csv file, each row of data is an index "i"
    #everytime we go to a new row, we frist convert that row to a list using split
    #we then only print that row if the index has a "P"

#create for loop to read only rows who have "F":
for line in inputFileTwo:
    lineSplit = line.split()
    if(lineSplit[2] == "F"):
        print(line)


        
inputFileTwo.close()
