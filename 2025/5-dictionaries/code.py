states = {
    'GA':'Georgia', 
    'FL': 'Florida', 
    'CA':'California', 
    'AR':'Arkansas'
    }

# Print the entire dictionary
print(states)

# Print only the keys
print(states.keys())

# Print only the values
print(states.values())

# Print the items (same as the first "print(states)", but as a tuple)
print(states.items())

######################

# Bill was tasked to split based on username and domain name. Finish the script to accomplish that.

# Output:

# ['user', 'domain1.com']
# ['user', 'domain2.com']
# ['user', 'domain3.com']
# ['user', 'domain4.com']

li = ["user@domain1.com","user@domain2.com","user@domain3.com","user@domain4.com"]

def splitter(input):
    for i in input:
        print(i.split('@'))

splitter(li)

######################

# Assign the following two lists to any variable names you like. Add the two lists together and print the combination.

# [1,2,3,4,5]

# ["hi","hello","hey"]

li1 = [1,2,3,4,5]
li2 = ["hi","hello","hey"]

def concat(a, b):
    print(str(a + b))

concat(li1,li2)

######################

# Write a Python script to print the length of the string representation of each element in a list of items called MyList. 

# ExampleList = [1,2,"aba", "bab"]

# Output: 

# 1
# 1
# 3
# 3

# Here is your list :)
MyList = [1, 2, "aba", "bab", "cab", "Length of this list shouldn't matter", "Your logic is key", "Account for integers, please"]
# Enter your code below this line please.

def stringRep(input):
    for i in input:
        print(len(str(i)))

stringRep(MyList)

######################

# Write a Python script to print the dictionary values sorted from smallest to largest. 

di = {5: 1, 4: 3, 2: 2, 6: 9, 3: 4}

di_values = di.values()

print(sorted(di_values))

######################
# Write a script that prints out only unique values from the list. 
li = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5,5,5]

di = set(li)

print(list(di))

######################
# Write a script to iterate through a set and print each item of the set on a separate line.

s = {1,2,3,4,5,6,7}

def lineomatic3000(input):
    for i in input:
        print(i)

lineomatic3000(s)
