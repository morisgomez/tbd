#PARSING XML DATA INTO PYTHON FILE:
#parsing data: to convert from format to another. 
#turning XML data to something we can work with in python.

import xml.etree.ElementTree as ET #need xml module to work w/ xml data.

#create a path to the xml file so we can get data:
pathToFile = "groceries.xml"

#use .parse function to parse the xml tree:
xmlTree = ET.parse(pathToFile)
#xmlTree holds access to the tree as an object.

#get the root of the tree:
treeRoot = xmlTree.getroot() #root is the element titled "grocery_list"
print(treeRoot)

#how would we traverse the tree if we have root access?
allGrocItems = treeRoot.findall("grocery_item") #puts each item into a list.

itemsOverSix = [] #empty list to push items over $6.

for grocItem in allGrocItems:
    name = grocItem.find("name").text #at each item, find element titled 'name' and access the text in that element.
    price = grocItem.find("price").text
    if float(price) > 6.00: #turn price from str to float to then compare.
        itemsOverSix.append(name) #add item name to empty list.

print(itemsOverSix) #prints list.