#!/usr/bin/env python3.7

count = 0                # The count starts with a value of 0
while(count < 101):      # This loop will keep cycling until "count" is under 100
    if count % 3 == 0:
        print ("fizz")
    elif count % 5 == 0:
        print ("buzz")
    else:
        print(count)     # This will print a number of asterisks equal to the value of "count"
    count += 1           # This will add one to the total of "count", per cycle