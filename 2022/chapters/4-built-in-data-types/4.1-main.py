#!/usr/bin/env python3.7

### --- Strings --- ###
input("Let's start with strings. Press enter to start...")

print("This is a string") # Can be used with double quotes
print('This is a string') # Or single quotes

# At REPL:
# """
# Multi
# Line
# String
# """

print("Ha" * 4) # Prints 4 Ha's

# Use String Methods (https://docs.python.org/3/library/string.html)
lower = "capitalized"
upper = lower.capitalize()
print(upper)

# Print a string on two lines
print("New\nLine")

# If you want to use the backslash in a string, you have to use two:
print("bin\\bash")

# If you want to use quotes in your string, you have to use slashes:
print('\'Quote\' This')
# Alternatively:
print("'Quote' That")

### --- Numbers --- ###
input("Math time! Press enter.")
# Addition +
# Subtraction -
# Multiplication *
# Modulus % (The remainder, after division)
# Exponent **
# Floor Division // (Truncate after division. For example, 5//2 = 2 as opposed to 2.5)
# Are operands equal: ==
# Are operands not equal: !=
# Are operands not equal: <> (extremely similar to !=)
# Is the left operand bigger than the right operand: >
# Is the left operand smaller than the right operand: <
# Is the left operand bigger or equal to the right operand: >=
# Is the left operand smaller or equal to the right operand: <=

2 + 2
10 - 4
3 * 9
5 // 3
5 % 3
2 ** 3
pow(2,3)
1.1 + 3
1.2 + 0.8

# To find out if you have an even number, do % (modulo) 2, and if the number is zero, it's even.
def isItEven(num1):
  if num1 == 0:
      print("Pick a number besides zero. ")
  elif num1 % 2 == 0:
      print(num1,"is an EVEN number!")
  else:
      print(num1,"is an ODD number!")
      
var1 = int(input("Give me a number and I'll tell you if it's even or odd: "))
isItEven(var1)

### --- Variables --- ###
input("Now we're onto variables. Press enter to start...")
my_name = "Joe"
print(my_name)
my_name + " Schmoe"
print(my_name)
print(my_name + " Schmoe")
my_name += " Schmoyoho"
print(my_name)

### --- Sequences --- ###
# Sequences include Lists, Tuples, and Ranges.
input("Lists, Tuples, and Ranges, OH MY! Press enter to start...")

# Lists are MUTABLE
my_list = [1,2,3,4,5]
print(my_list)          # Outputs the list
print(my_list[0])       # Outputs the first value in the list
print(my_list[4])       # Outputs the last value in the list
print(my_list[0:2])     # Outputs everything between the first and third value on the list
# print(my_list[start:stop:step])
print(my_list[0:5:2])   # Outputs everything between the first and sixth place in the list, skipping every other value
print(my_list[::-2])    # Reverses the list
len(my_list)            # Prints length of the list
len("ExampleString")    # Prints how many characters are in this string
my_list[0] = "A"        # Changed first value from a 1 to an A
print(my_list)          # Outputs the list with updated first value
my_list.remove("A")     # Removes first value in list
print(my_list)          # Prints list with missing first value
my_list.pop()           # "Pops" out the last value on the list. It will no longer be in the list.
print(my_list)          # Prints list with "popped" last value

# Tuples are IMMUTABLE
# They are not as useful as Lists, but can be useful for "coordinates"
point = (2.0, 3.0)          # Imagine this is an x,y coordinate
print(point[0])             # This will print the first value (x coordinate), which is 2.0
point_3d = point + (4.0,)   # Appends a third value to assume a point in 3D space. The comma has to be there.
print(point_3d)             # Prints new value with appended z coordinate
x,y,z = point_3d            # Assigns values to x, y, and z coordinates respectively
print(x)                    # Prints x coordinate value (which is 2.0)

# Ranges
print(range(10))            # This will print the starting and stopping values in the range
print(list(range(10)))      # This will print every single number between 0 and 9 out
print(list(range(1,12,2)))  # Start at 1, end at 12. Only output every other number.

### --- Dictionaries --- ###
# With lists, the indexes are NUMBERED. With Dictionaries, the indexes are NAMED
input("Time for some NAME-CALLIN' with DICTIONARIES. Press enter to start...")
ages = {'kevin': 29, 'alex': 29, 'bob': 40} # Kevin is 29, Alex is 29, Bob is 40
print(ages)                                 # Prints everything that was input
print(ages['kevin'])                        # Only outputs Kevins age
ages['keith'] = 29                          # Adds Keith and his weight to the dictionary
print(ages)                                 # Prints everyones (including Keith's!) weights
ages['keith'] = 30                          # Oops. We messed Keith up. This changes his age.
print(ages)                                 # Double check the age is right now.
del ages['bob']                             # Bob is so old we're not counting his age any more. DELETE!
print(ages)                                 # Poof, no more Bob
print(ages.pop('alex'))                     # You can also give Alex a POP
print(ages)                                 # Poof, Alex is gone. Just like so.
print(ages.get('kevin'))                    # This only queries someones age, then puts the person back