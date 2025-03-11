#/usr/bin/python3
# This program will print a status of your house, depending on the combination of positional (required) and optional arguments provided by the user
import argparse # importing the module argparse

house_damage = argparse.ArgumentParser()
#print(dir(house_damage)) # <---- uncomment if you want to see all the methods/attributes of the house_damage argument parser variable

house_damage.add_argument("street_number", metavar="STREET_NUMBER", type=int, help="Please put your house number for this argument") # This adds a positional (required) argument to house_damage called 'street_number' which displays 'STREET_NUMBER' in the help output. It must be an integer and will display the help text as well.

house_damage.add_argument("street_name") # adds another positional argument called 'street_name'

house_damage.add_argument("--broken", "-b", metavar="DAMAGE_TYPE", help=" Please put in the type of damage you have here", type=str) # adds your first optional argument, which can be called using '--broken', or '-b'. It will be stored as '.broken' Metavar, help, and type have been added for additional functionality and context for the user.


arguments = house_damage.parse_args() #This actually parses the arguments provided by the user. If none is provided by the user, it is stored as the keyword None.
if arguments.broken == None:    # This checks to see if the broken argument has the value of None, meaning the homeowner had nothing broken.
    print(f"Your house at {arguments.street_number} {arguments.street_name} is totally fine")   # This uses the parsed argument values stored in the arguments variable to print our formatted and customized string.
    
else:   # since arguments.broken must have a value, then the homeowner must have identified damage. So we'll execute this block.
    print(f"Looks like you have {arguments.broken} broke at your home address, {arguments.street_number} {arguments.street_name}. Might want to get that checked out.") # This puts together all our parsedSome  argument values stored in arguments for our sweet format printing.
    
# A practical use case:

# bad_ip.py log_file.log --threshold 
# print all IP addresses that have authentication failures above a certain threshold

# check_hash.py -sd starting_directory -fn file_name HASH
# starts at starting_directory (or current if nothing provided) and checks hash value of found files with matching file_name to see if it matches the HASH required parameter. If no file_name is provided, it will check every file's hash and let you know if it find a file with a matching HASH provided by the user.
