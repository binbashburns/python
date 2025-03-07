#################################

strng = 55
assert strng == str(strng), "String is not string."

#################################

# What error will the following code produce?

strng = "Toby, why are you the way you are?"

def func(strng):
    strng = strng.title()
  print(strng)
func(strng)

#################################

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug("About to enter while loop")
count = 0
while count <= 10:
    logging.debug(f"{str(count)}")
    count += 1

#################################

try: 
    for i in range(num):
        print(i)
except: 
    print("Out of range!")

#################################