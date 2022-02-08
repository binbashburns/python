#!/usr/bin/env python3.7

count = 0                # The count starts with a value of 0
while(count < 101):      # This loop will keep cycling until "count" is under 100
    if count % 3 == 0:   # If the count is divisible by three...
        print ("fizz")   # ... print "fizz"
    elif count % 5 == 0: # Else, if the count is divisible by five...
        print ("buzz")   # ... print "buzz"
    else:                # If the count isn't equal to either of those values
        print(count)     # Just output the number you're on
    count += 1           # And every time you do this loop, increment the count by 1.