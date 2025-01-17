#PARSING TXT DATA INTO PYTHON FILE:
#parsing data: to convert from format to another. 
#turning data to something we can work with in python.
txtFile = "groceries.txt"

#opening txt file:
openedTxt = open(txtFile, "r")

#reading file and storing in content variable.
content = openedTxt.read()
#read() does not parse the data. it makes it all into a single string.
#split(",") is what parses the data into list(s)

#prints the single line of data from file.
print(content)

#parse data into a list so we can work with it in python.
parsedData = content.split(", ") #each index in the list is created when reaching a comma.
#split() only usable for strings.

#print the list or parsed data.
print(parsedData)
#['apples', 'bananas', 'carrots']

#access an index from listl
print(parsedData[2]) #carrots.

#loop through list:
#for i in content: #i is each char in the entire line of data.
    #print(i)       #it's better to loop through it once it has been "split()"

for i in parsedData:
    print(i) #prints each index. 

#last step is to close the file bc opened the manual way.
openedTxt.close()