# Argparse 

# What is Argparse?

# It allows one to write a python script that allows for command line parsing

# First import argparse

import argparse

# Creates an instance of argparse which allows for the command line interface
# Can add in parameters such as prog, description, and epilog (text that displays after the help)
# parser = argparse.ArgumentParser()

# Example with parameters: (TO RUN: python3 main.py TEST -h)
# parser = argparse.ArgumentParser(
#                     prog='TEST',
#                     description='Description of the program',
#                     epilog='Explaination in help')

# # Runs the parser
# parser.parse_args()


# Adding arguements 

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

parser = argparse.ArgumentParser()
tack = parser.add_argument_group()
tack.add_argument("-a", "--add", help="Adds the numbers together", action="store_true")
tack.add_argument("-s", "--sub", help="Subtracts the numbers together", action="store_true")

parser.add_argument("num1",help="First Number",type=int)
parser.add_argument("num2",help="Second Number",type=int)

p = parser.parse_args()

if p.add:
    print(add(p.num1, p.num2))
if p.sub:
    print(sub(p.num1, p.num2))