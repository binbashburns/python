# Dictionaries

- A `dict()` (dictionary) is an ordered collection of entries.

- Each entry contains a `key:value` pair.

- Think of Webster's dictionary. The word is the `key` and the definition is the `value`

- Dictionaries maintain their order of insertion - Last In, First Out (LIFO).

- Dictionary keys have to be both unique and hashable. In other words a key can NOT be duplicated

More on dictionaries can be found at:
- [W3Schools](https://www.w3schools.com/python/python_dictionaries.asp)
- [Python Docs](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Creating Dictionaries

Two ways to create a dictionary, using `dict()` or `{}`

```
# Creating an empty dictionary
dictionary = dict()
dictionary2 = {}
```
```
# Example 1 (using {}):
names = {"key_1": "Bill", "key_2":"Jill", "key_3":"Gill"}
numbers = {1:1, 2:2, 3:3}

# Example 2 (using dict()):
also_names = dict(key_1 = "Bill", key_2 = "Jill", key_3 = "Gill")
also_numbers = dict(one = 1, two = 2, three = 3)  #NOTE: using this process will NOT allow you to assign integers as keys
```

## Accessing Items In A Dictionary

The `key` is the primary means of access when using a dictionary

Consider this: Would you open Webster's dictionary looking for a specific definition (`value`) in order to find the word (`key`) that it is assigned to? Or, would you look up a specific word (`key`) to find the definition (`value`) it is assigned to?

Access the names dictionary and print the name 'Bill'
```
names = {'key_1': 'Bill', 'key_2': 'Jill', 'key_3': 'Gill'}

print(names['key_1'])

#output:  Bill
```
Now access the dictionary and save the name 'Jill' to the variable: `name_2`
```
name_2 = names['key_2']
print(name_2)

#output:  Jill
```
- Dictionaries also have a .get() method that can be used to retrieve the value for a given key.

- `dict_name.get(key, default)`

- If a value for default is not provided, the None object will be returned.

```
print(names.get('key_1'))
#output:  Bill

#access a key that does not exist
print(names.get('key_10'))
#output: None

#provide a unique 'error message' to the .get()
print(names.get('key_10','Key does not exist'))
#output:  Key does not exist
```

## Finding Keys/Values

- The `in` and `not in` operators can be used to determine if a specific `key` or `value` exists in the dictionary.

- Both operators will return a `True` or `False` value.

- When used with the entire `dictionary`, the operators search for the `value` in the `keys` of the `dictionary`.

- The view returned by the values method can be used to search for a `value` in the values of the dictionary.

```
numbers = {'one':1, 'two':2, 'three':3}

# Using in and not in
print("one" in numbers) 
#output:  True          
print("one" not in numbers) 
#output:  False
```

## Adding and Updating Key:Value Pairs

   - Dictionaries are designed as a data structure that provide fast look-ups into the structure by key. Sub-script notation can be used to add new key/value pairs and to modify existing values for a given key.

   - `dict_name[key]` will retrieve the value associated to the given key.

   - If the key does not exist, a `KeyError` exception is raised

   - `dict_name[key] = value` will either add a new `key:value` pair, or modify the `value` associated to the given key.

Using the `names` dictionary, add two more keys and names

```
names['key_4'] = 'Phil'
print(names)
names['key_5'] = 'Will'
print(names)

#output: 
# {'key_1': 'Bill', 'key_2': 'Jill', 'key_3': 'Gill', 'key_4': 'Phil'}
# {'key_1': 'Bill', 'key_2': 'Jill', 'key_3': 'Gill', 'key_4': 'Phil', 'key_5': 'Will'}
```

Update the `value` of `key_1` to be the name 'Hill'

```
names['key_1'] = 'Hill'
print(names)

#output:
# {'key_1': 'Hill', 'key_2': 'Jill', 'key_3': 'Gill', 'key_4': 'Phil'}
```

## Removing Key Values/Pairs

   - Removing elements from a dictionary can be done by using the `del` keyword and through the `pop()`, `popitem()` methods.

   - `del dict_name[key]` removes the specified key/value pair from the dictionary, the key/value pair is not returned.

   - `del dict_name` deletes the entire dictionary.

   - The general syntax for the `pop()` method is as follows: `value_variable = dict_name.pop(key, default)`

   - `Key` represents the actual key of the key/value pair to attempt to remove.

   - `Default` represents an optional value to return if key does not exist. If left blank and the key does not exist in the dictionary a `KeyError` will be raised.

   - The general syntax for the `popitem()` method is as follows. `a_tuple = dict_name.popitem()`

   - The `popitem()` method takes NO arguments. It simply removes and returns the last `key/value` pair as a `tuple`, but raises a `KeyError` if obj is empty.

   - A tuple is an immutable collection of ordered elements.

Use the names and numbers dictionaries to practice using the `del` keyword and .`pop()` and `.popitem()` methods.

   - Pop key_1 off of names

```
names = {'key_1': 'Bill', 'key_2': 'Jill', 'key_3': 'Gill', 'key_4': 'Phil', 'key_5': 'Will'}
numbers = {1:1, 2:2, 3:3}

remove_key_1 = names.pop("key_1",None)  #You can use the None obj                       
print(names)

#output:
# {'key_2': 'Jill', 'key_3': 'Gill', 'key_4': 'Phil', 'key_5': 'Will'}
```

   - Pop something that does not exist
```
remove_key_10 = names.pop('key_10', 'Key does not exist') #You can use a unique 'error message'
print(remove_n4)

#output:  Key does not exist
```

   - Use `popitem()` to remove the last `key:value` pair in the dictionary until nothing exists in the dictionary

```
remove_3 = numbers.popitem()
print(numbers)  
#output: {1: 1, 2: 2}

remove_2 = numbers.popitem()
print(numbers)  
#output:  {1: 1}

remove_1 = numbers.popitem()
print(numbers)  
#output:  {}

remove_0 = numbers.popitem()
#output: KeyError: 'popitem(): dictionary is empty'
```

## Dictionary Methods - Continued

   - When there is a need to work with all `key/value` pairs in a dictionary, the following methods are useful.

   - The `.keys()` method returns a view of the dictionary keys.

   - The `.values()` method returns a view of the dictionary values.

   - The `.items()` method returns a view of the dictionary items.

   - Each item in the view returned by `.items()` is a 2 item `tuple` consisting of a `key` and a `value`.

   - Each of the views can also be converted to a `list` or a `tuple` by passing the view to a `list()` or `tuple()` constructor.

Create a new `dictionary` that uses state abbreviations as the `key` and the full name as the `value`.

### .keys()
```
state_keys = states.keys()
print(state_keys)

#output:  dict_keys(['GA', 'FL', 'CA', 'AR'])

#turn it into a list object

state_keys = list(state_keys)
print(state_keys)

#output:  ['GA', 'FL', 'CA', 'AR']
```
### .values()
```
state_values = states.values()
print(state_values)
#output:  dict_values(['Georgia', 'Florida', 'California', 'Arkansas'])
```
### .items()
```
state_items = states.items()
print(state_items)
#output:  dict_items([('GA', 'Georgia'), ('FL', 'Florida'), ('CA', 'California'), ('AR', 'Arkansas')])
```
## Looping/Iterating Through A Dictionary

Use the states dictionary to practice iterating over dictionaries

```
states = {'GA':'Georgia', 'FL': 'Florida', 'CA':'California', 'AR':'Arkansas'}

for each_thing in states:
    print(each_thing)

#output:  GA
#         FL
#         CA
#         AR
```

NOTICE that the `key` is returned. It can be helpful to change `each_thing` to the word `key`. `key` is not a reserved keyword for Python and it will not interfere with any dictionary operations.

Loop over the dictionary and print only the value
```
for value in states.values():
    print(value)

#output:  Georgia
#         Florida
#         California
#         Arkansas
```
Loop over the dictionary and print the key, value pair together
```
for item in states.items():
    print(item)

#output:  ('GA', 'Georgia')
#         ('FL', 'Florida')
#         ('CA', 'California')
#         ('AR', 'Arkansas')
```
NOTICE this output is a `tuple` consisting of the `key` and `value`

There are many different ways to accomplish the same outcome. The following examples show how many different ways you can loop over a dictionary and print the following `str`: 'The state of {full name} is abbreviated: {abbreviation}.'

   - Using only the `key`
```
    for key in states:
        print(f'The state of {states[key]} is abbreviated {key}')
```
   - Using the pairs of items
```
for item in states.items():
    print(f'The state of {item[1]} is abbreviated {item[0]}')
```
   - Using the `.items()` again, just a little different
```
for key, value in states.items():
    print(f'The state of {value} is abbreviated {key}')
```
Scenario:
How much would the luckiest person on Earth win if they got the winning number on ALL of the lotteries found in the dictionary below??
```
lottery = {'Mega Millions': 11111111111, 'Georgia Lottery': 222222222,'Power Ball': 3333333}
```
Print the sum of all values

# Sets

## About Sets

   - Sets are not ordered, do not allow for duplicates, and all items must be immutable.
   - To create a set use `set()`
   - `s = set()`
   - Sets also allow for different data types.

More on sets can be found at:

   - [W3Schools](https://www.w3schools.com/python/python_sets.asp)
   - [Python Docs](https://docs.python.org/3/tutorial/datastructures.html#sets)

```
s = {1, 2, 3, False, "String"}
print(s)
#output:  {False, 1, 2, 3, 'String'}

#turning a tuple into a set
s_two = set((1, 2, 3, False, "String"))
print(s_two)
#output:  {False, 1, 2, 3, 'String'}
```

## Adding items to a set

   - `set_name.add()` - Requires only 1 argument and adds the item into the `set` in no particular order

```
s = {1, 2, 3, False, "String"}

s.add(10)
print(s)
#output:  {False, 1, 2, 3, 10, 'String'}

s.add(50)
print(s)
#output:  {False, 1, 2, 3, 50, 10, 'String'}
```

Add an item to the set that already exists. Will it create a duplicate or an error???

```
s.add(50)
print(s)
#output:  {False, 1, 2, 3, 50, 10, 'String'}
```

No errors are raised and a `set` doesn't allow duplicates, it simply executes the line of code and continues on to the next line of your code.

## Removing items from a set

   - `set_name.remove()` Requires only 1 argument and removes the item if found in the `set`. If it is not found a `KeyError` will be returned.

```
s = {False, 1, 2, 3, 50, 10, 'String'}
s.remove(2)
print(s)

#output:  {False, 1, 3, 50, 10, 'String'}
```

## Set Methods - Continued

   - `set_name_1.difference(set_name_2)` - Accepts multiple arguments and returns what is found in set_name_1 that is not found in any of the sets provided in the arguments

   - `set_name_1.intersection(set_name_2)` - Accepts multiple arguments and returns what is found in ALL of the sets provided.

   - `set_name_1.union(set_name_2)` - Accepts multiple arguments and returns a compiled set of ALL items found in all of the sets provided.

Scenario:
The following are set objects contain collections of information that the Brigade security office uses to track A and B Company's soldiers and their clearance level.
Use set.methods() to find the following requested information:

### .union()
```
A_company = {'Nelson', 'Scott', 'Miller', 'King', 'Walker', 'Green', 'Jones', 'Hall', 'Campbell'}
B_company = {'Smith', 'Holly', 'Taylor', 'Martin', 'Jackson', 'Lewis', 'Lee', 'Moore'}
secret_clearance = {'Smith', 'Taylor', 'Lewis', 'Lee', 'Moore', 'Miller', 'Walker', 'Green', 'Jones', 'Hall', 'Campbell'}
ts_clearance = {'Taylor', 'Lee', 'Moore', 'Walker', 'Green', 'Campbell'}
```
Print a `set` containing ALL the names of people found in A Co and B Co, regardless of their clearance level
```
all_soldiers = A_company.union(B_company)
print(all_soldiers)

#output:  {'Lewis', 'Taylor', 'Miller', 'Hall', 'Walker', 'Scott', 'Lee', 'Martin', 'Jackson', 'Nelson', 'Smith', 'Green', 'Campbell', 'Moore', 'Jones', 'King', 'Holly'}
```
### .difference()
Who in B Co does NOT have a TS clearance?
```
B_TS_uncleared = B_company.difference(ts_clearance)
print(B_TS_uncleared)

#output:  {'Jackson', 'Smith', 'Martin', 'Lewis', 'Holly'}
```
Who in A Co has NO clerance?
```
A_uncleared = A_company.difference(secret_clearance,ts_clearance)
print(A_uncleared)

#output:  {'Scott', 'King', 'Nelson'}
```
### .intersection()
```
A_company = {'Nelson', 'Scott', 'Miller', 'King', 'Walker', 'Green', 'Jones', 'Hall', 'Campbell'}
B_company = {'Smith', 'Holly', 'Taylor', 'Martin', 'Jackson', 'Lewis', 'Lee', 'Moore'}
secret_clearance = {'Smith', 'Taylor', 'Lewis', 'Lee', 'Moore', 'Miller', 'Walker', 'Green', 'Jones', 'Hall', 'Campbell'}
ts_clearance = {'Taylor', 'Lee', 'Moore', 'Walker', 'Green', 'Campbell'}
```
Who in A Co at least has a SECRET clearance?
```
A_secret = A_company.intersection(secret_clearance)
print(A_secret)

#output:  {'Miller', 'Hall', 'Walker', 'Green', 'Campbell', 'Jones'}
```
### Combining methods
```
A_company = {'Nelson', 'Scott', 'Miller', 'King', 'Walker', 'Green', 'Jones', 'Hall', 'Campbell'}
B_company = {'Smith', 'Holly', 'Taylor', 'Martin', 'Jackson', 'Lewis', 'Lee', 'Moore'}
secret_clearance = {'Smith', 'Taylor', 'Lewis', 'Lee', 'Moore', 'Miller', 'Walker', 'Green', 'Jones', 'Hall', 'Campbell'}
ts_clearance = {'Taylor', 'Lee', 'Moore', 'Walker', 'Green', 'Campbell'}
```
