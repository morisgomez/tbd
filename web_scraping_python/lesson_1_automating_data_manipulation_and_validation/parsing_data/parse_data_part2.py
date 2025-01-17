#PARSING CSV DATA INTO PYTHON FILE:
#parsing data: to convert from format to another. 
#turning csv data to something we can work with in python (lists).

import csv #need csv module to work w/ csv data.

#create a path to the csv file so we can get data:
pathToFile = "groceries.csv"

#open the file:
openedCSV = open(pathToFile, "r")

#step 1: read file:
#bc we are using csv module, we open the csv file in a different way than before.
#readFile = openedCSV.read() would not be appropiate in this case. 

#reading csv file using csv module:
#csv's reader() parses the csv data into lists.
readFile = csv.reader(openedCSV)

#step 2: print each line of data using for loop.
next(readFile) #this skips the first line of headers when looping.
#line starts at the 2nd line in csv file. 

emptyList = [] #empty list to append each line from file.

for line in readFile:
    #note: each line of data is read as a list with 2 strings.
    #we need to convert the # from each line/list into an int type.
    line[1] = int(line[1]) #convert each num from str to int from each line.
    emptyList.append(line) #appending the line to the emptyList.
    print(line)
    #print(line[0] + ", " + line[1])

print(emptyList) #a list with sub lists of str and int values.

#step 3: close file.
openedCSV.close()