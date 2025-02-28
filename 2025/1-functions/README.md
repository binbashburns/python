# Defined Functions you are familiar with already

- `print()`
- `input()`

## Creating Functions

- To define a unique new function, use the keyword def followed by a function name followed by a parenthesized list of parameters, if needed, followed by a colon.

- A function must be defined before it can be used (called).

- A function in Python defines a block. As with other blocks in Python (if/elif/else statements, and while/for statements) the code must be indented by using all spaces or all tabs.

```
def function_name(parameter1, parameter2): #  With parameters

def function_name():                       #  Without parameters
```

## Calling Functions

A function call calls the function that is defined which will execute what is in the function. When a function is called, the arguments are the data passed into the method’s parameters.

```
# Creating a function called function_name
def function_name(parameter1, parameter2):
   print(parameter1, parameter2)
   #end of function

# Creating two variables and calling the function
parameter1 = ["This", "is", "a", "argument"]
parameter2 = ("This is another argument")

function_name(parameter1, parameter2) #  This is where the function is ‘called’
#Output:  ['This', 'is', 'a', 'argument'] This is another argument
```

## Arguments

- Arguments passed to Python functions may be of any type.

- It is the programmer’s responsibility to ensure that the type of data passed is appropriate for how the data is used in the function.

```
# Defining a function with a single parameter
def function(para1):
   print("An argument was passed to this function: ", para1)

# Function call and passing in an argument
function([1,2,3])
```

- Argument data is assigned to parameters.

- Python treats assigning arguments to parameters as assignment, meaning that Python does not copy the argument data into the parameters (recall that in Python, assignment never copies data).

- Positional parameters are bound to argument data by their position in the function definition.

```
def func(num1, num2):
   print(num1,num2)

func(num1= 1, num2=2)
#output 1 2
```

## Returning Data

- Functions often return values via the return statement.

- It is common to save returned values for later use BUT if it is not needed, the function call is equivalent to the returned value when used by the calling code.

```
# Creating a function and returning the output
def func_1(num):
   return num

print(func_1([1,2,3]))

#Output:  [1, 2, 3]
```

- The `print()` function will simply provide a copy of the function's results/output

- The `return` keyword will actually provide a value that can be assigned to a variable and used

```
def new_func(param1):
    return param1.upper()

return_value = new_func('hello world')
print(return_value.split())
#output:  ['HELLO', 'WORLD']
```

# Name Scopes

    Functions provide a nested namespace (sometimes called a scope), which localizes the names they use, such that names inside the function won’t clash with those outside (in a module or other function). We usually say that functions define a local scope, and modules define a global scope.

## The four Python scopes:

1. The `local` scope are names created inside a function.

2. The `enclosed` scope are names created in a function that encloses (contains) another function. This section includes some examples of names defined in the enclosed scope.

3. The `global` scope are names created inside a script outside of any/all functions.

4. The `built-in` scope are names that Python reserves for its own internal workings.

5. When Python looks to resolve (use) a name, it examines the scopes 'inside-out'.

6. Python looks at the most restrictive scope first and works its way outward to increasingly larger scopes.

7. Pythonistas express this concept as the `LEGB` rule.

8. Python looks first in local scope, followed by enclosed, followed by global, followed by builtin (LEGB).

9. Each function contains its own scope; if a Python program has six functions that program contains six local scopes. The scope is activated when the function is called and disappears when the function terminates (either normally or abnormally).

10. A function cannot change the value of data bound to a name outside its scope (without some extra work). If a Python function uses the name defined in global (or any enclosing) scope, Python creates a new name known only in the local scope and binds data to it.

```
# Example of local scope
def func():
   within_function = "This is locally defined"
   print(within_function)

func()
# Output: This is locally defined 
```

```# Example of a Enclosed Scope
# Creating a function and defining num
def func_1():
   num = 20
   # Creating a function and printing num and num2
   def func_2():
       print(num)
       print(num2)
   func_2()   
num2 = 50
func_1()
#output:
#20
#50
```

- The name `num2` is defined (known) in the global scope. Functions may access names outside their scope provided the scope is an outer scope (E, G or B scopes). 

```
#Global Scope
# Declaring a global variable
global_var = "I am global"

# Creating a function and changing global_var
def func_1():
   global_var = "New global"
   print(global_var)

# Creating a function and printing global_var
def func_2():
   print(global_var)

func_1()
func_2()

#output: 
#New global
#I am global
```

# Building Custom Functions - Examples

## Example 1

Python allows you to build your own custom function to accomplish tasks.

Starting with something simple, build a function that multiplies 2 and 4 and return the product

```
def multiply():
    return 2 * 4
#output:  8
```

This function is hardcoded to ONLY multiply 2 and 4.

Make a new function modified to accept two arguments/parameters so that it can multiply ANY two numbers passed into the function.

```
def multiply(num1, num2):
    return num1 * num2
```

## Example 2

Build a function called username that accepts two parameters/arguments. Those arguments will be a person's first name and last name.

The function should return a formatted string that looks like the following: `last.first`

```
def username(first, last):
    return f"{last}.{first}"
```