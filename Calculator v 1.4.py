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
def input_number(x):#Function to check if the user inputs a number.
    while True:
        try:
            return int(input(x))
        except ValueError:# If anything is typed except for a number the valueerror will show up.
            print("That was not a number")  
def sqrt(x):#square root function. making use of the math module.
    x = math.sqrt(sqrtnum)
    return x   
while True:# while loop to make it restart as long as the condition is met. 
    choice = input_number("****  +    1  ****\n****  -    2  ****\n****  *    3  ****\n****  /    4  ****\n***squareroot? 5**\n****give pi? 6****\n****  quit 7  **** \nchoose what to do: ")
    choice1 = int(choice)#user input is converted to an integer.
    if choice1 == 7:
        print ("Thanks for trying!!!!!")
        sys.exit()# If the user chooses 6 the program will use the moudule sys to stop the while loop.
    elif choice == 6:
        print (math.pi)
    elif choice1 == 5:# if the user wishes to find out the square root of a number. the program will go through this itteration.
        sqrtnum = input_number("Enter a number: ")# here i ask for a number that the user wishes to know the square root of.
        if sqrtnum > 0:
            print ("The square root of", sqrtnum,"is", sqrt(sqrtnum))#square root function is called.
            print ("")# space to make it look nicer
        else:
            print ("you can't use a negative number")
            sqrtnum = input_number("Enter another number: ")# I ask again for a number so the user may correct him/herself.
            print ("The square root of", sqrtnum,"is", sqrt(sqrtnum))  
    elif (choice1 == 1 or choice1 ==  2 or choice1 ==  3 or choice1 ==  4):
        num1 = input_number("Enter first number: ")# the is for the input when the user want to do adding, substracting, multiply or devision.
        num2 = input_number("Enter second number: ")#Two number are asked.     
        
        if choice1 == 1:
            print ("",num1, "+" ,num2, "=", add(num1, num2))#adding function being called
        elif choice1 == 2:
            print ("",num1, "-" ,num2, "=", substract(num1, num2))#substracting fucntion being called       
        elif choice1 == 3:
            print ("",num1, "*" ,num2, "=", multiply(num1, num2))#multiply function being called
        elif choice1 == 4:
            if (num1 != 0 and num2 != 0):# to make sure the user is not trying to divide by zero. if the user still tries that the program will just restart the loop.
                print ("",num1, "/" ,num2, "=", devision(num1, num2))#devision function being called.
            else:
                print ("Can't divide by ZERO")        
        print ("")  #just a space to make it look nicer.  
