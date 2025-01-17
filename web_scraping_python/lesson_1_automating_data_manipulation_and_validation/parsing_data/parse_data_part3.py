#PARSING JSON DATA INTO PYTHON FILE:
#parsing data: to convert from format to another. 
#turning JSON data to something we can work with in python.

import json #need json module to work w/ JSON data.

#create a path to the json file so we can get data:
pathToFile = "groceries.json"

#open the file:
openedJSON = open(pathToFile, "r")

#read the file:
readFile = openedJSON.read()

#parse the data from JSON into something python can use:
parsedData = json.loads(readFile)
#json's loads() parses the json data into a dictionary.
#parsedData has value of a dictionary. 

#access a key-value pair in dictionary:
print(parsedData["apples"]) #2

#note: indexes to access data in lists 
#but key-value pairs in dictionaries.

#close file:
openedJSON.close()