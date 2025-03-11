#/usr/bin/python3
# This program will take any number of numbers as user arguments and print the sum of them (and other parts so you can see it happen.) Feel free to remove print statements as you see fit.

import sys              # importing the sys module
args = sys.argv         # assigning the contents of the sys.argv to a list called args
print(type(args))       # printing the type of args to show it's a list
print(args[0])          # args[0] is always the filename
print(args, end='\n\n') # printing the entire list of args, ending with two newlines for visibility

if len(args) < 2:       # Checking to make sure I have more than the file name, since 
    print(f"Give me some more numbers please.")

else:
    numbers = args[1:]      # using slicing to grab all command line arguments starting after the file name to the end so we have all our argments
    print(numbers)          # printing the newly assigned list
    true_nums = list(map(int,numbers))  # map runs a specified function across an iterable (or container). We are assigning a list of all the strings in numbers converted to an integer to the variable true_nums
    print(true_nums)                    # printing true_nums so we can see the conversion
    print(sum(true_nums))               # the sum function takes all integers in an iterable and adds them together. Here we are just printing the results of the sum function ran against the list of true_nums





# if len(args) < 2:
#     print("Please provide me all the numbers you want the sums of. Try again")
# else:
#     numbers = map(int, args[1:])
#     print(f"The sum of all your numbers is {sum(numbers)}!")