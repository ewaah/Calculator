import math
import sys
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

while True:# while loop to make it restart as long as the condition is met.
    
    choice = input("****  +    1  ****\n****  -    2  ****\n****  *    3  ****\n****  /    4  ****\n***squareroot? 5**\n****  quit 6  **** \nchoose what to do: ")
    if choice == '6':
        print ("Thanks for trying!!!!!")
        break# If the user chooses 6 the program will use the break handler to stop the while loop.
    
    if choice == '5':
        num = input_number("Enter a number: ")# here i ask for a number that the user wishes to know the square root of.
        goodinput = False
        if num < 0:
            while not goodinput:
                try:
                    num = int(input('Please enter a positive number: '))
                    if num > 0:
                        goodinput = True
                        print ("square root of", num, "=", math.sqrt(num))
                        choice = input("****  +    1  ****\n****  -    2  ****\n****  *    3  ****\n****  /    4  ****\n***squareroot? 5**\n****  quit 6  **** \nchoose what to do: ")# i copied the choice line so the loop would restart and the user can choose again.
                        if choice == '6':
                            print ("Thanks for trying!!!!!")
                            sys.exit()
                    else:
                        print("that's not a positive number. Try again: ")
                except ValueError:
                    print("that's not an integer. Try again: ")
        else:
            print ("square root of", num, "=", math.sqrt(num))# math.sqrt function being called and used.
            choice = input("****  +    1  ****\n****  -    2  ****\n****  *    3  ****\n****  /    4  ****\n***squareroot? 5**\n****  quit 6  **** \nchoose what to do: ")# i copied the choice line so the loop would restart and the user can choose again.
            if choice == '6':
                print ("Thanks for trying!!!!!")
                sys.exit()
    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")#input_number is a fucntion to make the program crash safe. if the user entered a letter it gives a message and asks for the number again.
    # the user can input a second number here. integers aswell as floats.
    # all of the below makes use of the fucntion defined above and the input given by the user. after that
    # it gets printed out for the user to see.
    
    if choice == '1':
        print ("",num1, "+" ,num2, "=", add(num1, num2))
    
    elif choice == '2':
        print ("",num1, "-" ,num2, "=", substract(num1, num2))
    
    elif choice == '3':
        print ("",num1, "*" ,num2, "=", multiply(num1, num2))
    
    elif choice == '4':
        print ("",num1, "/" ,num2, "=", devision(num1, num2))
    
    else:
        print ("Invalid choice, pick another one.")
    print ("")  #just a space to make it look nicer.  
    
    