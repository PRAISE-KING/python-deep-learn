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
    """This function takes a name as input and prints a greeting message."""
    print(f"Hello, {name}! Welcome to the world of functions.")

greet("PRAISEKING")