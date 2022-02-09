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
    else:                                   # If the result is over zero and over 15, it prints this
        print("Positive greater than 15")
elif test < 0:
    print("Negative")
else:
    print("ZERO")
    
