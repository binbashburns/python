#!/usr/bin/env python3.7
import random

print("Pick a name from a hat!")
print("Think of 5 names, and input them one at a time.") 
input("Once the last name is input, the program will randomly select a winner! Press Enter to start...")

list = []
count = 0
while(count < 5):
    number = str(input("Please input a name: "))
    list.append(number)
    count += 1
random.shuffle(list)
print("And the winner is...",list.pop(),"! Congratulations!")
print("Sorry",list,"maybe next time!")