#!/usr/bin/env python3.7
### --- Functions --- ###
def hello_world():                          # You don't *have* to pass arguments in to a function. It is optional.
    print("Hello World!")

hello_world()                               # This calls the function at runtime.

def print_name(name):                       # This creates a function called print_name, which passes in a value "name"      
    return print(f"Name is {name}")         # Using interpolation, passes the name in as a input

print_name("Bob")                           # print_name function, with the name "Bob" input as a variable

# Return
def add_two(num):                           # Defines function "add_two" which passes in one variable, "num"
    return num + 2                          # Returns "num" plus two

result = add_two(2)                         # Creates variable, whose value is the product of add_two, passing in 2 as variable
print(result)                               # Outputs product of the "result" variable

def add(num1, num2):
    return num1 + num2
print(add(1,5))

# Positional Arguments v. Keyword Arguments
def contact_card(name,age,car_model):
    return f"{name} is {age} and drives a {car_model}"
print(contact_card("Bob",34,"Civic"))                       # This performs the function assuming the variables are in the right place
print(contact_card(age=34,car_model="Civic",name="Bob"))    # You can also do this so it doesn't matter what order it's in.

# Default Arguments
def can_drive(age, driving_age=16):         # Sometimes you want to set static values that will not change in a function
    return age >= driving_age               # This checks if the variable provided is greater than or equal to 16
print(can_drive(15))                        # Since the variable passed to the function is less than 16, it returns False
print(can_drive(15, 14))                    # This will evaluate to True because we've specified a different value for driving_age