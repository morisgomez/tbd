#goal: how do you automate input validation from users?

import pyinputplus as pyip
#imprt library needed to handle input automation.
#words to right of "as" are the alias for library.

#EXAMPLE 1: Integer Selection.
print("\nEXAMPLE 1") #\n means new line like in C++.

#result will store input of user:
result = pyip.inputInt("Enter num of bags for items:", min = 0)
#inputInt only takes an integer as input.

print("You will use", result, "store bags.")
#prints result.

#EXAMPLE 2: Menu Selection.
print("\nEXAMPLE 2")

resultTwo = pyip.inputMenu(["red", "green", "blue"], lettered = False, numbered = True) 
#will ask user to choose option based on number. then store that as string in resultTwo.

print("You have chosen a", resultTwo, "marker.")

#EXAMPLE 3: Email Selection.
print("\nEXAMPLE 3")

resultThree = pyip.inputEmail("enter email")

print("The email you entered:", resultThree)