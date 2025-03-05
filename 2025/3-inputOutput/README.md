# Input / Output

## File Overview
To handle files in Python, there are three key things to know:

`open()` `read()` or `write()` `close()`

```
# open file in write mode, and store it in a variable
file_obj = open("info.txt", "w")

# write to a file
file_obj.write("Hello World")

# close the file
file_obj.close()
```

## Opening Files

- Performing file input/output operations is, arguably, one of the most important features of a programming language.

- Fortunately, Python has language features that greatly facilitate this important task.

- Use the `open()` function to prepare a file for I/O operations.

### Specify:

- File name as string or path expression. The name/path may be absolute or relative.

- Remember, for Windows OS, the is the path separator versus the / which is the path separator for Linux/Mac.

### File Modes

Mode options allow for the ability to read or write to a file. Some modes require two characters while others only require one. The list below shows all the available mode options:

| Keyword |	Description|
| --- | --- |
|r |	reads from file, this is used by default|
|w |	writes to a file, will overwrite if file exists|
|a |	appends to a file, will not overwrite|
|x |	creates a file if it does not exist|
|b |	allows for reading or writing to binary|
|t |	text mde, can read or write|
|w+ or r+ |	file must eist, can read and write|

## How to open a file in python

To open a file, use the `open()` function. Put either the file or the path in the parenthesis, followed by the mode. Below are examples of opening files and storing them in a variable. 

```
# Create a file object and open file in read mode
file_obj = open("info.txt", "r")

# Create a file object and opens file in write mode
file_obj = open("info.txt", "w")

# Create a file object and opens file in append mode
file_obj = open("info.txt", "a")

# Create a file object and opens file in read binary mode
file_obj = open("info.dat", "rb")

# Create a file object and opens file in write binary mode
file_obj = open("info.dat", "wb")

# Create a file object and opens file in append binary mode
file_obj = open("info.dat", "ab")
```

## Reading Files

To read one line at a time, open the file and use the `read()` method `read()` returns a string of all the contents from file

```
# open file in read mode, and store it in a variable
file_obj("info.txt")

# reading from a file
file_content = file_obj.read()

# close the file
file_obj.close()
```

`readline()` reads one line of the text file at a time.

```
# With automatically closes file
with open("info.txt") as file_obj:
   print(file_obj.readline())
```

`with` is used to do everything that has been taught but NOW there is no need to close because it **automatically** does it

The `readlines()` method returns the whole text file in the form of a list!

```
# Opening info.txt and reading the lines
with open("info.txt") as file_obj:
   file_content = file_obj.readlines()
   print(file_content)
```

- When using the `readlines()` method, it returns a list of strings from the file.
    
- The readlines will also return the new line character \n, but there is a way to remove it as shown below: 

```
# Opening info.txt and reading the lines
with open("info.txt") as file_obj:
   file_content = file_obj.readlines()
   # Creating an empty list
   li = []
   # Iterate through the list
   for i in file_content:
       # Stripping the new line character
       li.append(i.strip())
   # Iterate through the new list
   for j in li:
       # print out the new list
       print(j)
```

## Writing Text to a File
`write()` - writes a single string to a file `writelines()` - writes a list of strings to a file, does not add newlines

```
data = [("California", 39937489, "Sacramento"),
       ("Texas", 29472295, "Austin"),
       ("Florida", 21992985, "Tallahassee")]

with open("info.txt", "w") as data_obj:
       for state, population, capital in data:
           data_obj.write(f'{state}, {population}, {capital}\n')
```

Note: If info.txt was already created, using 'w' mode will overwrite the file. Using 'a' will not overwrite the file, it will add the contents to the end of the file.

```
# open file in write mode, and store it in a variable
file_obj = open("info.txt", "w")

# write to a file
file_obj.write("Hello World")

# close the file
file_obj.close()
```

```
# open file in append mode, and store it in a variable
file_obj = open("info.txt", "a")

# write to a file
file_obj.write("Hello World")

# close the file
file_obj.close()
```

## Closing Files
- A Python program could open a file, do the I/O operations, and close the file by issuing Python functions.

- The `close()` method closes the file and may be explicitly coded as shown in the listing below.

- Python will automatically close files when I/O operations are done in concert with the with statement.

- Remember with closes the file automatically

## Seek and Tell
- The Python functions `seek()` and `tell()` allow a program to navigate the read/write pointer in a file and to report on the current position of the read/write pointer.

- `seek( pos )` to position file at position pos for next I/O operation.

- For example, `seek(0)` positions the read/write pointer to the beginning of the file. The `seek()` function takes an optional second parameter called whence which is an integer specifying where to start seeking from.

- `seek( pos, whence )` when whence = 0 (the default value) tells Python to advance the pointer at the start of the file.

- For example, the call `seek( 100, 0 )` tells Python to advance the read/write pointer 100 characters from the start of the file.

- `seek( pos, whence )` when whence = 1 tells Python to advance the pointer at the current read/write position.

- For example, the call `seek( 100 )` followed by `seek(10, 1 )` tells Python to _first advance 100 characters from the start of the file followed by advancing 10 characters from the current position, which is 100.

- `seek( pos, whence )` when whence = 2 tells Python to advance the pointer first to the end of the file, then back up the read/write position by pos characters.

- In short, whence = 2 tells Python to move the read/write pointer from the back of the file.

- The `tell()` function returns an integer specifying the current position within the file of the read/write pointer.

```
# Open a file and print tell
with open("info.txt") as file_obj:
  print(file_obj.tell())
```

```
# Open a file and print tell
file_obj = open("info.txt")

# Setting the pointer to beginning of file
file_obj.seek(0,0)

# Printing the first line
print(file_obj.readline())

# Closing the file
file_obj.close()
```

