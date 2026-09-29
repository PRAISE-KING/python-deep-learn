# functions - are reusable blocks of code that perform a specific task. They help in organizing code, making it more readable, and avoiding repetition.
# there are two types of functions in Python: built-in functions and user-defined functions.
# built-in functions are pre-defined functions that come with Python, such as print(), len(), and range(). User-defined functions are created by the programmer to perform specific tasks.
# there are two types of user-defined functions: functions with parameters and functions without parameters. Functions with parameters take input values, while functions without parameters do not take any input values.
# the syntax for defining a function in Python is as follows:
# def function_name(parameters):
#     # function body
# # the function body contains the code that performs the specific task. The function can return a value using the return statement.

# some important points to note about functions in Python are:
# 1. Functions can have default parameter values, which are used if no argument is provided for that parameter.
# 2. Functions can return multiple values using tuples, lists, or dictionaries.
# 3. Functions can be nested, meaning that one function can be defined inside another function. 
# 4. Functions can be assigned to variables, passed as arguments to other functions, and returned from other functions.
# 5. Functions can have variable-length arguments, which allow them to accept an arbitrary number of arguments. This is done using the *args and **kwargs syntax.
# 6. Functions can have docstrings, which are used to document the purpose and behavior of the function. Docstrings are enclosed in triple quotes and can be accessed using the help() function.
# 7. Functions can be recursive, meaning that they can call themselves. This is useful for solving problems that can be broken down into smaller subproblems.
# 8. Functions can be defined in modules, which are separate files that contain related functions. Modules can be imported into other Python programs using the import statement.
# 9. Functions can be decorated, which means that they can be modified or enhanced using decorators. Decorators are functions that take another function as input and return a new function with modified behavior.
# 10. Functions can be tested using unit tests, which are automated tests that verify the correctness of the function's behavior. Unit tests can be written using the unittest module in Python.
# 11. Functions can be used to implement object-oriented programming concepts, such as encapsulation and inheritance. In Python, functions can be defined as methods within classes, allowing them to operate on the attributes of the class instances.
# 12. Functions can be used to implement functional programming concepts, such as higher-order functions and closures. Higher-order functions are functions that take other functions as input or return functions as output, while closures are functions that capture the local variables of their enclosing scope.

def greet(name):
    """This function takes a name as input and prints a greeting message.""" # decostring - describes what the fuction is all about.
    print(f"Hello, {name}! Welcome to the world of functions.")

greet("PRAISEKING")  # Output: Hello, PRAISEKING! Welcome to the world of functions.



# sources of functions in python
# 1. built-in functions:
print('built-in functions: input(), len(), type(), range(), print()')  # Output: built-in functions: input(), len(), type(), range(), print()

# 2. user-defined functions: created by the programmer
def add_numbers(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b    

result = add_numbers(5, 3)
print(result)  # Output: 8  

# 3. functions from modules: are impoted then used in the program.
import math
result = math.sqrt(16)
print(result)  # Output: 4.0
print(math.ceil(7.6))  # math.floor() rounds down to the nearest integer, while math.ceil() rounds up to the nearest integer. Output: 8


#   TYPES OF FUNCTIONS 
# 1. Functions with parameters: take input values
# 2. Functions without parameters: do not take any input values
# 3. Functions with default parameter values: use default values if no argument is provided
# 4. Functions that return multiple values: can return tuples, lists, or dictionaries
# 5. Nested functions: can be defined inside another function
# 6. some have no output, some have output, some have parameters, some don't have parameters, some have both output and parameters, some have neither output nor parameters.

#   PARAMETERS AND ARGUMENTS
# parameters are variables that are defined in the function definition and are used to pass values to the function when it is called. 
# Arguments are the actual values that are passed to the function when it is called. The number and order of arguments must match the number and order of parameters in the function definition.

# def fun_name(parameters): - function definition
# fun_name(arguments) - function call

def clean_text(text):
    print(text.strip().lower())
    
clean_text(' coMe heRE MAMA   ') # Output: come here mama


# local variables are variables that are defined inside a function and can only be accessed within that function. They are created when the function is called and destroyed when the function returns.
# global variables are variables that are defined outside of any function and can be accessed from anywhere in the program. They are created when the program starts and destroyed when the program ends.

f = 2 # global variable

def multiply(x):  # x is a parameter
    y = x * f  # y is a local variable
    print(y)
    
multiply(5)  # 5 is an argument
# Output: 10


the_rule = 'n/a' # global variable

def rules():
    the_rule = 'follow the rules' # local variable
    print(the_rule)

rules() 
print('the rule is : ',the_rule) # output: the rule is : n/a => this takes the global variable because the local variable is only accessible within the function.


    # POSITIONAL AND KEYWORD ARGUMENTS
# positional arguments are passed to a function in the order in which they are defined in the function
# keyword arguments are passed to a function using the name of the parameter, allowing them to be passed in any order.

def bio(first_name, last_name, age):
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    full_name = first_name + ' ' + last_name
    print(f"My name is {full_name} and I am {age} years old.")


bio(" john ", " doe ", 30) # positional arguments
bio(age=25, first_name="jane", last_name="smith")  # keyword arguments
bio("  alice  ", last_name="  johnson  ", age=28) # mixed arguments - positional arguments must come before keyword arguments.

# .capitalize()  → "hello WORLD" → "Hello world"
# .title()       → "hello WORLD" → "Hello World"
# .upper()       → "hello WORLD" → "HELLO WORLD"
# .lower()       → "hello WORLD" → "hello world"


