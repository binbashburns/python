# Standard Libraries

## The import Keyword

The keyword `import` is useful for literally importing standard Python (and other third-party) libraries (also known as Modules).

These modules/libraries give access to a multitude of other tools/functions/methods that can be useful to a program but aren't necessary for basic Python execution.

More information about `import` can be found at:

[GeeksforGeeks](https://www.geeksforgeeks.org/import-module-python/)

[W3Schools](https://www.w3schools.com/python/python_modules.asp)

[Python Docs](https://docs.python.org/3/reference/simple_stmts.html#import)

## Basic Libraries

We will only scratch the surface of Python's available libraries. For a more complete list of standard and other third-party libraries you can visit [Python Docs - The Python Standard Library](https://docs.python.org/3/library/index.html)

### Where Python Standard Libraries Live?

When Python is downloaded onto your system a group of standard libraries are included for programmers to use as needed. The following code will show you the directories in which those libraries live.

```
import sys

print(sys.path)
```

You can explore the random library that should be found in the `/usr/lib/python3.8` directory.

### Math Library/Module

The `math` library/Module provides access to multiple functions/methods that house commonly used formulas and values for math operations

Pi is a great example of one of these values

Import the math library and access the value of Pi

```
import math
print(math.pi)

#output:  3.141592653589793
```

Use the `dir()` built-in function for a full listing of functions available from the math library/module

```
dir(math)  #NOTE: if you are starting in a new python file/code block, you will need to import math again
```

Try out the square root function/method of the math library

```
import math

num = math.sqrt(25)
print(num)

#output:  5
```

## Random Library/Module

The `random` library/module is great for making pseudo-random selections from either a range of numbers or collections of items.

Python Docs warns programmers that this module should not be used for security purposes and suggests the use of the [secrets](https://docs.python.org/3/library/secrets.html#module-secrets) library/module instead.

Test out the random library on the list of names below to return a random name for bathroom cleaning duty!

```
names = ['Smith', 'Barnes', 'Perry', 'Johnson']

import random

bathroom_duty = random.choice(names)
print(bathroom_duty)
```

Execute this code a few times to see how the name changes

The random library is also great at choosing a random number out of a range of numbers you can specify by using the `.randint(start, stop)` method/function. The start and stop values must be `int` and ARE inclusive.

```
import random

num = random.randint(5, 10)
print(num)
```

If you don't need to import the entire contents of a library/module, python does allow you to import a specific method/function.

Import just the `choice` method/function from the `random` library/module.

```
from random import choice

lst = [1,2,3,4,5,6]
x = choice(lst)
print(x)
```

Maybe you don't like the name of the method/function, python also allows you to alter it upon import.

Import the `randint` method/function and call it `RANDnum`

```
from random import randint as RANDnum
y = RANDnum(1,100)
print(y)
```

There are so many more libraries/modules available that can be useful for so many things. Later, in networking we will revisit this topic!