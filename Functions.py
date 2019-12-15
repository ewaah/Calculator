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
