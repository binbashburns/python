# Modifying, and methods of Lists and Tuples

## Modify items in a list using indexing

Lists are mutable and can be modified dynamically

```
lst = [1,2,3]
#change the first item (found in index 0) to the string 'one'

lst[0] = 'one'
print(lst)
#output: ['one', 2, 3]
```

## List Methods

The most commonly used methods are listed below, however, there are many more methods available. To learn more about other list methods you can visit both of the following resources:

- Using help(list) in your IDE

- Python Docs - More on Lists

W3Schools

- `append(item)` - Adds a new element to the end of the list, increasing the length by one.

- `count(item)` - Returns the total number of times the item specified is found inside the list.

- `extend(iterable)` - Adds each element from the iterable passed in as new elements to the end of the list, increasing the length by the number of items in the iterable.

- `insert(index, item)` - Adds the specified item at the specified index position, shifting existing elements to make room for the new item, increasing the length by one.

- `pop(index)` - Deletes the element at the specified index or the end of the list if no index is provided, decreasing the length by one.

- `remove(value)` - Deletes the first instance of the specified value in the list, decreasing the length by one.

## Methods in action:

Adding an item to the list (three ways):

`list.append()`

```
lst = [1,2,3]
lst.append(4)  #NOTE: .append can only take ONE item at a time
print(lst)
#output:  [1, 2, 3, 4]
```

`list.extend()`

```
lst = [1,2,3]
new_lst = [4,5,6]
lst.extend(new_lst)
print(lst)
#output:  [1, 2, 3, 4, 5, 6]
#NOTE: lst is permanently changed and new_lst has remained unchanged
```

`list.insert()`

```
lst = [1,2,3]
lst.insert(0,'zero')
print(lst)
#output:  ['zero', 1, 2, 3]
```

Removing items from a list (three ways):

`list.remove()`

```
lst = [1,2,3,1,2,3]
lst.remove(1)
print(lst)
#output: [2, 3, 1, 2, 3]
#NOTE: ONLY the first instance of the int 1 was removed
```

`del keyword`

```
lst = [1,2,3]
del lst[0]  #NOTE:  del is a keyword used to delete items from the list
print(lst)
#output: [2, 3]
```

`list.pop()`

```
lst = [1,2,3]
lst.pop(0)
print(lst)
#output: [2, 3]

lst = [1,2,3]
lst.pop(1)
print(lst)
#output: [1, 3]
```

Counting items in a list:

`list.count()`

```
lst = [1,2,3,4,5,1,2,3]
lst.count(1)  #NOTE: This method returns a number than CAN be saved into a variable
one_count = lst.count(1)
print(one_count)
#output:  2
```

# Tuple Methods

Tuples are NOT mutable and cannot be dynamically changed using methods. Tuples do still have some helpful methods.

- `count(item)` - Returns the total number of times the item specified is found inside the tuple

- `index(item)` - Returns the index position of the item

```
tup = (9,8,7,9,8,7)
tup.count(9)
nine_count = tup.count(9)
print(nine_count)
#output: 2
```

```
tup = (1,2,3)
tup.index(2)  #NOTE: The returned index number can be saved into a variable if needed
where_is_2 = tup.index(2)
print(where_is_2)
#output:  1
```

## Make changes to a tuple

While tuples are great at maintaining the integrity of its contents, sometimes a change may need to be made.

*Scenario*:
Joe Smith is being reassigned to Ft. Eisenhower, GA and his record needs to be updated

```
soldier_159 = ('Joe','Smith','88M','Ft. Drum, NY')
soldier_159 = list(soldier_159)  #converting to a list to access mutable properties
soldier_159[-1] = 'Ft. Eisenhower, GA'
soldier_159 = tuple(soldier_159)  #converting back to a tuple to 'lockdown' or deny mutability
print(soldier_159)
#output:  ('Joe', 'Smith', '88M', 'Ft. Eisenhower, GA')
```
# String Methods - Part 1

- Strings in Python are an ***immutable*** sequence of zero or more characters.

- Literal string values may be enclosed in single or double quotes and can span multiple lines in several ways.

    - This is achieved by using the line continuation character as the last character.

- Literal strings may also be prefixed with a letter r or R.
    
    - These are referred to as raw strings and use different rules for backslash escape sequences.

- Strings in Python are represented using a class named `str`.

- The str class has an abundance of methods defined within it.

    - Some of the methods return Boolean values such as `True` or `False`.

    - Some methods return a modified **copy** of the string.

- A full listing of the string methods can be found by using:

    - `help(str)` from the Python interactive shell or your IDE.

    - [W3Schools](https://www.w3schools.com/python/python_strings_methods.asp)

    - [Python Docs](https://docs.python.org/3/library/stdtypes.html#string-methods)

## String Casing methods

- Python provides several methods that can be used to modify the casing of characters in a string.

- `upper()` returns a **copy** of the string with all cased characters converted to uppercase.
- `lower()` returns a **copy** of the string with all cased characters converted to lowercase letters.

- `casefold()` similar to lower(), is stronger, more aggressive, meaning that it will also convert unicode characters into lower case. This method will find more matches when comparing two strings and both are converted using the casefold() method

- `title()`returns a **copy** of the string with the first letter of each word in the string in upper case and the rest of the characters in lower case.

- `capitalize()` returns a **copy** of the string with the first letter in upper case and the rest of the characters in lower case.

```
string = "python is fun"                                                        #Output: 
print("String is now upper:", string.upper())           #String is now upper: PYTHON IS FUN
print("String is now lower", string.lower())            #String is now lower python is fun
print("String is now casefold:", string.casefold())     #String is now casefold: python is fun
print("String is now title:", string.title())           #String is now title: Python Is Fun
print("String is now capitalize:", string.capitalize()) #String is now capitalize: Python is fun
```

# String Methods - Part 2

## Finding Substrings

- A variety of methods can be used to find instances of characters or strings within another string.

- `count(s)` will return the number of times the value passed to the method is found within the string.

- `index(s)` will return the index position of the first instance of the value passed to the method.

- `index()` will raise a ValueError exception if the value to find is not found within the string

- `find(s)` is similar to index but find will return a -1 when the sub-string is not found rather than raising an exception.

```
string = "python is fun"
                                # Output:
print(string.count("n"))        #  2
print(string.index("n"))        #  5
print(string.find("n"))         #  5
print(string.find('z'))         #  -1
```

# String Methods - Part 3

## Methods To Create Modified Copies of Strings

Methods can be used to clean up data or to replace or remove unwanted characters.

**It is important to note that all of these methods will only return a modified copy of your string UNLESS you assign it to a variable**

- `strip() `will remove any leading and trailing whitespace from the string.

- `lstrip()` will remove any leading whitespace (whitespace on the left)

- `rstrip()` will remove any trailing whitespace (whitespace on the right)

- `replace(old, new)` replaces all instances of the first parameter with all instances of the second parameter.
    
    - An optional third parameter can be used to specify the number of times the replacement is to be made.

```
s = "\t 123-456-7890 \t"
                                          #Output:
stripped = s.strip()
print(s)#-------------------------->    123-456-7890
print(stripped)#-------------------------->123-456-7890
print(stripped.replace("-", " "))#-------->123 456 7890
```

## Splitting and Joining Strings Working With Lists

Strings are immutable objects which can make them difficult to easily alter. Let's look at some methods available to break apart strings, make some alterations if necessary, and then join them back together.

- `.split()` - Returns a `list` of the original string elements separated by index by the item specified; default value is whitespace

```
phrase = 'hello world'
split_phrase = phrase.split()
print(split_phrase)
#output:  ['hello', 'world']  NOTE: The output is a list object
```

It is important to note that the item provided to the `.split()` method will be removed completely from the string

```
python
sentence = 'Hello class! Welcome to Python.'
split_sentence = sentence.split('!')  #NOTE: the item provided MUST be a str value
print(split_sentence)
#output:   ['Hello class', ' Welcome to Python.']
```

Notice that the '!' is completely removed and the sentence has been split apart based on the placement of the '!'

Scenario:
Given a string with a first and last name, isolate and save each part of the name to separate variables

```
full_name = 'Joe Smith'
fname = full_name.split()[0]
lname = full_name.split()[1]
print(fname)
#output:  Joe
print(lname)
#output:  Smith
```

The `.split()` will break a string apart based on a specific character, however, what if you need to break a string apart to single out each letter?
Scenario:
Change the str 'jello' to 'hello' WITHOUT manually recreating the string

```
strng = 'jello'
str_lst = list(strng)
print(str_lst)
#output:  ['j', 'e', 'l', 'l', 'o']
```

Now that we have isolated each character into its own index within a list, how can we change the 'j' to an 'h'?

```
str_lst[0] = 'h'
print(str_lst)
#output:  ['h', 'e', 'l', 'l', 'o']
```

The change from 'j' to 'h' was successful, but it the string is still broken apart and a list data type; we need it back together as a str

- `.join()` - Returns a string value. NOTE: the syntax notes below for this method:
        
    - `'str'.join(iterable_item)` NOTE: iterable_item can be a `list`, `str`, or `tuple` (there are more data types than can be used with the join method)

Using our last value for `str_lst`, use the `.join()` to return a string with NO whitespace inbetween each character. ie: 'hello'

```
new_str = ''.join(str_lst)
print(new_str)
#output:  hello
```

Try different characters in the str portion of the `.join()` to see it working. What happens if you replace `''.join(str_lst)` with `'+'.join(str_lst)`?

# is METHODS for Strings

- Methods can be used to to validate if a string contains a certain set of characters

- When the method validates, it will return either True or False

## The methods are:

- `isdigit()`: will return True if all characters are digits
- `islower()`: will return True if all characters are lowercase
- `isupper()`: will return True if all characters are uppercase
- `isalnum()`: will return True if all characters are alphanumeric

```
s = "will this return true?"
print(s.islower())
#output:  True
print(s.isdigit())
#output:  False
print(s.isupper())
#output:  False
print(s.isalnum())
#output:  False         NOTE: This returned False because whitespaces do NOT count as alphanumeric characters
```

# Escape Characters
| *sequence* | *Character/Meaning* | 
|---|---|
| `\newline` | Ignored| 
| `\` | Bckslash| 
| `\'` | 	Single Quote| 
| `\"` | 	Double Quote| 
| `\a` | 	ASCII Bell(Bel)| 
| `\b` | 	Backspace| 
| `\f` | 	form feed| 
| `\n` | 	newline/Line feed| 
| `\r` | 	Carriage Return| 
| `\t` | 	Horizontal Tab| 
| `\v` | 	Vertical Tab| 
| `\ooo` | 	ASCII Character(octal value ooo)| 
| `\xhhh` | 	ASCII Character (Hex Value hhh)| 
| `\uxxxx` | 	Unicode Character with 16-bit hex alue xxxx| 
| `\Uxxxxxxx` | 	Unicode Character with 32-bit hex value xxxxxxx| 

```
single_quote = "This is a \'single quote\'" # The string will escape char for a single quote
print(single_quote)
#output:   This is a 'single quote'

new_line = "This: \n will produce a newline." # The string will produce a newline at the end of it
print(new_line)
#output:   This: will produce a newline

tab = "This is a \t tab" # The string will add a tab
print(tab)
#output:   This is a     tab

chess_piece = "\U0000265F" # Use unicode to create a chess piece
print(chess_piece)
#output:   ♟
```
```
                                                            #Output:
print("Strings are \'easy\' in Python")                     #Strings are 'easy' in Python

print(r"Strings are \'easy\' in Python")                    #Strings are \'easy\' in Python

print("Strings are \x27easy\x27 in Python")                 #Strings are 'easy' in Python

print('\U0000265F','\U0000265F','\U0000265F','\U0000265F','\U0000265F')#--> ♟ ♟ ♟ ♟ ♟
```

# String Formating

## f-string

- Python has several ways to format the output rather than just printing space separated values.

- The newest and easiest way to format a string for output in Python uses formatted string literals or f-strings.

- Beginning with Python 3.6, f-strings are available for output formatting.

- To use a formatted string literal, begin the `str` with f or F before the opening quotation mark.

- This can be used in front of single, double, or triple quotation marks.

- Inside the string, the programmer adds braces to hold values { }

```
coding_language = "Python"
print(f'{coding_language} is fun')   
#output:   Python is fun
```

- A programmer can define and merge f-strings to create a multi-line f-string.

- Notice that the `{name}`placeholder, or field can be repeated. Python evaluates the fields in the braces as Python expressions and looks for variables to match.

- The order of the fields does not matter and as stated earlier, a field can contain any valid Python expression. It is important to include the `f` or `F` in front of each line.

```
coding_language = "Python"
audience = "Students"

long_string = f"{coding_language} is fun. {audience} seem to enjoy learning Python"

print(long_string)
#output:  Python is fun. Students seem to enjoy learning Python.
```

- When using f-strings the programmer can place curly braces in a literal string.

- The curly braces can contain a Python expression.

- Additionally, the programmer can specify additional formatting details for the result of the Python expression.

- A format specifier can be appended to the field after a colon : and inside the curly braces.

- Backslashes are not allowed within the formatting field and will cause a syntax error!

|Type |	Meaning|
|---|---|
|`s` |	String format. This is the default type for strings and may be omitted.|
|`none` |	The same as 's'.|
|`b` |	Binary Format. The Number is display as base 2.|
|`c` |	Character. Converts the integer to a Unicode Character.|
|`d` |	Decimal Integer. This converts the number to base 10.|
|`x` or `X` |	Hex format. Display the number in base 16. The case of the hex number will match the case of the specifier.|
|`f` |	Fixed point number. Displays the number with a decimal point. Default precision is 6.|
|`%`|	percentage. Multiplies the number by 100 and displays in fixed ('f') format with a percent sign.|

```
PI = 3.14159
print(f"PI is now 2 decimal places: {PI:.2f}") #  this will show 2 digits after the decimal
#output:  PI is now 2 decimal places: 3.14

PI = 3.14159
print(f"PI is now 4 decimal places: {PI:.4f}") #NOTE rounding took place in the string formatting
#output:  PI is now 4 decimal places: 3.1416

num = .5
print(f"num is now a percentage: {num:%}") 
#output:  num is now a percentage: 50.000000%

print(f"num is now 2 decimal places: {num:.2%}") 
#output:  num is now a percentage with only 2 decimal places: 50.00%
```
## str.format() - Another way to do the same thing

- `format()` is a method to be used with str.

- Much like f-strings, the `str.format()` method uses curly braces in a template string to mark where the output should be replaced.

- The syntax is to create a string literal with fields marked with curly braces `{}` where the programmer wants the output to appear.

```
difficulty = "easy"
output = "Formatting in python is {}".format(difficulty)
print(output)       
#output:  Formatting in python is easy
```                      
```
task = "Formatting"
difficulty = "easy"
output = "{} in python is {}".format(task, difficulty)
print(output)
#output:  Formatting in python is easy
```
