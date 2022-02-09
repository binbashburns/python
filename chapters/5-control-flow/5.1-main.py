#!/usr/bin/env python3.7
### --- Conditionals and Comparisons --- ###
print(1 < 2) # This returns a boolean of whether this is true or not. This would evaluate to True
print(1 > 2) # This would return a "False"

# Comparison Operators
print("Addition +")
print("Subtraction -")
print("Multiplication *")
print("Modulus % (The remainder, after division)")
print("Exponent **")
print("Floor Division // (Truncate after division. For example, 5//2 = 2 as opposed to 2.5)")
print("Are operands equal: ==")
print("Are operands not equal: !=")
print("Are operands not equal: <> (extremely similar to !=)")
print("Is the left operand bigger than the right operand: >")
print("Is the left operand smaller than the right operand: <")
print("Is the left operand bigger or equal to the right operand: >=")
print("Is the left operand smaller or equal to the right operand: <=")

# In
print(2 in [1,2,3]) # This will evaluate to True, as there is a 2 in the list
print(4 in [1,2,3]) # This will evaluate to False, as there is no 4 in the list
print(4 not in [1,2,3]) # This will evaluate to True, as there is no 4 in the list

# If / Elif / Else
test = 1                # Establishes "test" with a value of 1
if test > 0:            # Start your statement with a condition. In this case, we're checking if "test" is greater than zero
    print("Positive")   # If "test" is greater than zero, it will print this
elif test < 0:          # You can have as many "elifs" in between as you need. This is checking if "test" is lesser than zero
    print("Negative")   # If "test" is lesser than zero, it will print this
else:                   # You have to end your conditional with an "else:" to give one last option to select.
    print("ZERO")       # If test is not greater or lesser than zero, it will print "ZERO"

# Now let's try another one, but nested
test = 1
if test > 0:                                # First layer of nesting. Evaluates if the number is > 0
    if test > 10 and test < 15:             # Second layer. Evaluates if the number, that we've identified > 0, is over 15
        print("Positive in range: 10 - 15") # If the result is over zero but under 15, it prints this
    else:                                   
        print("Positive greater than 15")   # If the result is over zero and over 15, it prints this
elif test < 0:
    print("Negative")                       # If the result is under zero, it prints "Negative"
else:
    print("ZERO")                           # If the result is not any of these, it will print "ZERO"
    
if True:                                    # This will automatically be evaluated as True
    print("Was true")                       # So it will print True
    
if 1 > 2:                                   # One is not more than two, so this will evaluate to...
    print("Was true")
else:
    print("Was false")                      # "Was false"
    
name = "Kevin"                              # Establishes a string variable called "name", whos value is "Kevin"
if len(name) >= 6:                          # If the amount of letters in "Kevin" is greater than or equal to 6...
    print("Name is long")                   # The name is long
elif len(name) == 5:                        # If the name is 5 letters long...
    print("Name is 5 characters")           # The name is 5 characters
elif len(name) >= 4:                        # If the amount of letters in "Kevin" is greater than or equal to 4...
    print("Name is 4 characters or more")   # The name is 4 characters or more
else:                                       # If the amount of letters in "Kevin" is not equal to any of these
    print("Name is short")                  # The name is short
    
# Or
first = ""                                  # Establishes a string variable called "first", which is blank
last = "Thompson"                           # Establishes a string variable called "last", which is equal to "Thompson"
if first or last:                           # If either of these fields has a value populated...
    print("The user has a part of a name")  # The user has at least part of a name

# And
first = "Bob"
last = ""
if first and last:
    print("The user has a full name")
else:
    print("The user does not have a full name")
    
# While Loop
count = 10              # The count starts with a value of 10
while(count > 0):       # This loop will keep cycling until "count" is below 0
    print("*" * count)  # This will print a number of asterisks equal to the value of "count"
    count -= 1          # This will subtract one from the total of "count", per cycle
    
count = 0               # The count starts with a value of 0
while(count < 10):      # This loop will keep cycling until "count" is over 10
    print("*" * count)  # This will print a number of asterisks equal to the value of "count"
    count += 1          # This will add one to the total of "count", per cycle
    
count = 1
while count <= 4:
    print("Loooping")
    count += 1
    
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}") # Prefix the string with f to interpolate
    count += 1
    
# For Loop
colors = ['blue','green','red','purple']
for color in colors:
    print(color)
    
for color in colors:
    if color == 'blue':     # Blue is first on the list, so it will...
        continue            # ...get skipped. It will not print, it will start the loop over.
    elif color == 'red':    # Green is the next color. Red isn't even reached yet before...
        break
    print(color)            # Green is printed, because the color was not blue, and it was not red
    
point = (2.1, 3.0, 7)       # Note, this is a (tuple), not a [list]
for value in point:
    print(value)            # Notice the result of this tuple is very similar to a list
    
ages = {'kevin':59, 'bob':40,'kayla':21} # Note, this is a {dictionary}
for key in ages:
    print(f"{key} is {ages[key]}")

for letter in "my_string":  # Note, this is a "string"
    print(letter)
    
list_of_points = [(1, 2),(2, 3),(3, 4)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")
    
