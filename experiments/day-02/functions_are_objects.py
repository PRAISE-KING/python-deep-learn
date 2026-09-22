# well cover what actually happens when python calls a function

# Functions are objects
# functions too contains id, reference names, and types

# ......................... EXERCISE 1 .........................
def greet():
    print('hello')
    
x = greet         # greet ----> is the function object
                  # x=greet makes x to be the same function object
                  # greet() -----> calls the function

print(type(x))

x()

# the diagram

        # greet
        #     |
        #     |
        # Function object
        #     --> type - function
        #     --> name - greet
        #     --> id - id(greet)
        #     --> instructions - print('hello')
        

# QUIZ

# What does x refer to?
    # x is bound to the same function object as greet
# What does type(x) print?
    # prints class function
# What happens when x() runs?
    # calls the function
# Draw the memory diagram.

        # greet / x
        #     |
        #     |
        # Function object
        #     --> type - function
        #     --> name - greet
        #     --> id - id(greet)
        #     --> instructions - print('hello')
        



