#description: using regular expressions to extra certain 
#characters from a string.

#import modules:
import re #re module to use regular expression functions.

#create the regular expression we want to extract:
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
#each '\d' represents a digit.

#create example string:
example = "The number is 123-456-9999."

#extract the regular expression from example:
result = phoneNumRegex.search(example)
#search for phoneNumRegex inside example.

print(result) #note: result is not T or F but works in similar way.

if(result): #matching expression exists.
    print("Phone number found:", result.group()) #group() gets the matching expression from string.
    print("Area code:", result.group()[0:3]) #get from index 0 to index 3 (area code).
else: #no matching expression exists.
    print("code failed.")

   