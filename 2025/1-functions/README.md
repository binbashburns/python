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