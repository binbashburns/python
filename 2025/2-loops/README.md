# RELATIONAL VS. LOGICAL VS. MEMBERSHIP OPERATORS

## RELATIONAL

```
print(5 < 10)
#output: True

print(5 >= 10)
#output:  False

print(5 == 5)
#output:  True

print(5 != 5)
#output:  False

print(5 is 5)  #works but isn't great practice
#output:  True
#<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?

print(type([1,2,3]) is list)
#output:  True
```

## LOGICAL

```
print(5 < 10 and 5 > 3)
#output:  True
print(5 < 10 or 5 > 3)
#output:  True

print(5 < 10 and 5 > 20)
#output:  False
print(5 < 10 or 5 > 20)
#output:  True
```

## MEMBERSHIP
```
lst = [1,2,3,4,5]

print(5 in lst)
output: True
```
```
lst = [1,2,3,4,5]

print(5 not in lst)
output: False

print(50 not in lst)
output: True
```

# CONDITIONALS

## IF

The fundamental decision making control structure in many programming languages is the if statement.

Code inside an if suite is only executed if a given condition is True.

The following examples demonstrate proper indenting when using the if statement and its variants.

Also, notice the required use of the colon : to end the header portion of the if statement.

```
number = 25

if number <= 25:
   print("number is smaller or equal to 25")        
#output: number is smaller or equal to 25
```

```
lst = [1,2,3,4,5]

if 5 in lst:
    print('5 is found in lst')
#output: 5 is found in lst

if 50 in lst:
    print('50 found in lst')
#output:                            
#  NOTE that there is NO output above becase the if statement does not evaluate as True

if 50 not in lst:
    print('50 not found in lst')
#output: 50 not found in lst
```

## ELSE
```
lst = [1,2,3,4,5]

if 50 in lst:
    print('50 found in lst')
else:
   print('50 was not found')
#output:     50 was not found
```

## ELIF
```
number = 25

if number <= 25:
   print("number is smaller or equal to 25")        

elif number == 50:
   print("number is 50")

elif number <= 75:
   print("number is less than or equal to 75")

else:
   print("number is greater than 75")

#output: number is smaller or equal to 25

# NOTE Change the integer value stored in number to see how the conditional blocks output changes
```

### Evaluate multiple conditions at once
```
num_1 = 10
num_2 = 0

if num_1 == 10 and num_2 == 0:
   print("num_1 is 10 and num_2 is 0")      
#output: num_1 is 10 and num_2 is 0


if num_1 == 10 or num_2 == 10:
   print("num_1 is 10 or num_2 is 10")      
#output: num_1 is 10 or num_2 is 10
```

### Logic errors with conditional blocks
```
grade = ui(int("Give me your Python grade: "))
if grade < 70:
    print('You fail. Sorry, but Cyber is not for everybody :(')
elif grade > 70:
    print('Congrats, you pass with a C')
elif grade > 80:
    print('Congrats, you pass with a B')
else:
    print('You get an A, smarty')

# NOTE  Enter a variety of grades to observe logic error
```

Logic Error solved:
```
grade = int(input("Give me your Python grade: "))
if grade >= 90:
    print('You get an A, smarty')
elif grade >= 80:
    print('Congrats, you pass with a B')
elif grade >= 70:
    print('Congrats, you pass with a C')
else:
    print('You fail. Sorry, but Cyber is not for everybody :(')
```

## Slicing
You have seen indexing that allows access to an individual item in a `list/tuple` or character in a `str`. There may be times you need to access more than one item or character at a time. Slicing gives you this ability.

Syntax:

`item_to_slice_from[start:stop:step]` Notice that these are colon `:` separated

The `start:stop:step` numbers are integers that represent the index values for the sequence being sliced from.

    NOTE: the `stop` value is EXCLUSIVE, which means it slices up to, but NOT including the index number provided.

Use slicing to print the first three items found in the following `list`:

```
lst = ['zero',1, 'two', 3, 'four', 5]

print(lst[0:3])
#output: ['zero', 1, 'two'] 
```

## Length

```
lst = [,1,2,3,4]
lst_len = len(lst)
print(lst_len)
#output:  4
```
```
str1 = 'Hello world'
str_len = len(str1)
print(str_len)
#output:  11
```
```
lst2 = [1,2,3,['a','b','c'],(9,'8',7)]
tup_len = len(lst2[-1])
print(tup_len)
#output:  3
```
```
lst1 = [1,2,3,4]
tup1 = ('hello', 'world')
str1 = 'Python was first released in 1991'
total = len(lst1) + len(tup1) + len(str1)
print(total)
#output:  39
```

## While
```
# Declaring a counter
counter = 1

# While the counter is less than or equal to 5 print counter
while counter <= 5:
    print(counter)
    counter += 1  #update the counter to prevent infinite loop
#output: 1
#        2
#        3
#        4
#        5
```
```
user_input = input()
user_list = []

while user_input:
   user_list.append(user_input)
   user_input = input()
   print(user_input)
```
```
while False:
   print('This code never executes')
```
```
while True:
   print('this will execute forever and ever and ever...')
```
## Break
- Any looping construct can have its control flow changed through a break statement within it.

- When a break is executed, control of the program jumps to the first statement beyond or outside the loop.

- A break is often used when searching through a collection for the occurrence of a particular item.

Update the previous while True loop to include a break:

```
while True:
    print('this will execute forever and ever and ever...')
    break
```

Using the while True loop, collect input from a user again until an empty str is collected. Append user input into a list.

```
lst = []
while True:
    ui = input()
    # if ui == '':
    if not ui:
        break
    else:
        lst.append(ui)

print(lst)
```

## For Loops

The `for` loop in Python is used to iterate over the items of any sequence, such as a `str`, `list`, `tuple`, or any iterable object.

The generic syntax of a `for` loop is: `for target in sequence`: suite

Each item in the sequence is evaluated once and assigns the item to the target and then the suite is executed.

The loop terminates after processing the last item in the sequence.

```
strng = 'hello world'

for each_letter in strng:
   print(each_letter)
#output: h
#        e
#        l
#        l
#        o
#              NOTE: this is whitespace that was in the original strng
#        w
#        o
#        r
#        l
#        d
```

```
lst = [1, 'two', 3, 'four']

for each_num in lst:
   print(each_num)
#output:  1
#        two
#        3
#        four
```

```
str_lst = ['this', 'is', 'a', 'list', 'of', 'words']

total = 0
for word in str_lst:
    total += len(word)

print(total)
#output:  18
```

```
names = ['bob', 'joe', 'sally', 'harold']

for each_name in names:
    if each_name == 'sally':
        print('we found sally!')
        break
    else:
        print(f'{each_name} is not sally')

#output:    bob is not sally
#           joe is not sally
#           we found sally!
```

```
data = [("California", 39937489, "Sacramento"),
       ("Texas", 29472295, "Austin"),
       ("Florida", 21992985, "Tallahassee")]

for each_item in data:
    print(each_item)

#output:  ('California', 39937489, 'Sacramento')
#         ('Texas', 29472295, 'Austin')
#         ('Florida', 21992985, 'Tallahassee')


for state, population, capital in data:
    print(f'the state of {state} has a population of {population} and its capital is {capital}')

#output:  the state of California has a population of 39937489 and its capital is Sacramento
#         the state of Texas has a population of 29472295 and its capital is Austin
#         the state of Florida has a population of 21992985 and its capital is Tallahassee
```

## Using Range and Length Functions Together

### Isolating and Indentifying Index Positions

#### range(len()) Functions working together

Using the `range()` and `len()` functions together is helpful when needing to iterate over a collection of items while also identifying which index position each item is in.

```
lst = ['zero','one','two','three']
for index_num in range(len(lst)):
    print(index_num)

#output:    0
#           1
#           2
#           3
```

Use the dynamic counting created by using `range(len())` to access the items inside the list

```
lst = ['zero','one','two','three']
for index_num in range(len(lst)):
    print(lst[index_num])

#output:    zero
#           one
#           two
#           three
```

**Scenario**:
Create a queue message to let everyone in the customers list know what position they are in. Use the index number their name is found in to assign their position number

```
customers = ['Jim', 'Bob', 'Sue', 'Mary', 'Allen']
Queue_message = ''

for position in range(len(customers)):
    Queue_message += f'{customers[position]} is in position {position}\n'

print(Queue_message)
#output:    Jim is in position 0
#           Bob is in position 1
#           Sue is in position 2
#           Mary is in position 3
#           Allen is in position 4
```

**Scenario**:
Given a `list` of names, print the names of people who are found at the even indexes. (Remember, zero counts as an even number in python)

#### enumerate() Function

The `enumerate()` accepts up to two arguments and is a function that returns an enumerate object that assigns numbers to each item found in an iterable object.

This built-in function is another way of accomplishing what the range(len()) function can also do.

`enumerate()` can be given a start int; by default when no int is supplied the function begins numbering items at 0.

Syntax:

`enumerate(iterable, start=0)`
```
lst = ['zero','one','two','three']

print(enumerate(lst))
#output:  <enumerate object at 0x000001BBE4859FC0>
```

The `enumerate()` function is like the `range()` function that creats a range object that by itself is not abundantly helpful. However, combining it with a `list()` conversion function or using it inside a for loop leverages the usefulness of this built-in function.

```
for num in enumerate(lst):
    print(num)

#output:    (0, 'zero')
#           (1, 'one')
#           (2, 'two')
#           (3, 'three')
```

Notice the output each time is a `tuple` of information consisting of the numbered item and the item itself from `lst`

Change the *start* value:

```
for num in enumerate(lst, 1):
    print(num)

#output:    (1, 'zero')
#           (2, 'one')
#           (3, 'two')
#           (4, 'three')
```