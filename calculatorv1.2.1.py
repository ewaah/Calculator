import math#Module being added to use square root.
import sys#Module being called to make it easier to exit to program from wherever i want. sys.exit() is used for this specific action.

def add (x, y):# adding function
    sum = x + y
    return sum
def substract (x, y):# substract function
    sum = x - y
    return sum
def multiply (x, y):# multiply function
    sum = x * y
    return sum
def devision (x, y):# devision function
    sum = x / y
    return sum
def input_number(x):# fucntion to make it crash safe
    while True:
        try:
            return int(input(x))
        except ValueError:
            print("That was not a number")            
def sqrt(x):#square root function. making use of the math module.
    x1 = math.sqrt(x)
    return x1

while True:# while loop to make it restart as long as the condition is met. 
    choice = input_number("****  +    1  ****\n****  -    2  ****\n****  *    3  ****\n****  /    4  ****\n***squareroot? 5**\n****  quit 6  **** \nchoose what to do: ")
    choice1 = int(choice)#user input is converted to an integer.
    
    if choice1 == 6:
        print ("Thanks for trying!!!!!")
        sys.exit()# If the user chooses 6 the program will use the moudule sys to stop the while loop.
        
    elif choice1 == 5:# if the user wishes to find out the square root of a number. the program will go through this itteration.
        x = input("Enter a number: ")# here i ask for a number that the user wishes to know the square root of.
        x1 = int(x) # the users inputs is converted to a integer.
        print ("The square root of", x,"is", sqrt(x1))#square root function is called.
        print ("")# space to make it look nicer 
    elif choice1 == (1 or 2 or 3 or 4):
        num1 = input_number("Enter first number: ")# the is for the input when the user want to do adding, substracting, multiply or devision.
        num2 = input_number("Enter second number: ")#Two number are asked.     
        
        if choice1 == 1:
            print ("",num1, "+" ,num2, "=", add(num1, num2))#adding function being called
        elif choice1 == 2:
            print ("",num1, "-" ,num2, "=", substract(num1, num2))#substracting fucntion being called       
        elif choice1 == 3:
            print ("",num1, "*" ,num2, "=", multiply(num1, num2))#multiply function being called
        elif choice1 == 4:
            print ("",num1, "/" ,num2, "=", devision(num1, num2))#devision function being called      
        elif choice1 == 5:
            print (sqrt(x1))#square root function being called        
        else:
            print ("Invalid choice, pick another one.")
        print ("")  #just a space to make it look nicer.  
