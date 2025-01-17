try:
    userInput = int(input("enter number:")) #i thought you needed a module to work with use inputs in python?

    quotient = 10 / userInput 
    #if the userInput is not an int, run valueError exception.
    #if the userInput is a zero, run ZeroDivisionError.

    print("10 divided by your input is:", quotient) #this line only runs if there are no exceptions.
except ValueError:
    print("please enter an integer type.")
except ZeroDivisionError:
    print("cannot divide by zero.")

#notice the different terms from C++: no use of 'throw'